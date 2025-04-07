class Board:
    """A list of cell objects, representing the board made of 9x9 cells"""

    def __init__(self):
        self.all_cells = self.setup_board()
    
    def setup_board(self):
        """Setup the board from cell objects"""

        all_cells = []
        for row in range(9):
            for col in range(9):
                all_cells.append(Cell(row,col))

        return all_cells

class Cell:
    """Represent one cell in the board"""

    def __init__(self, pos_r, pos_c):
        self.pos_r = pos_r
        self.pos_c = pos_c
        self.num_list = [n+1 for n in range(9)]
        self.block = self.gen_block_id()

    def gen_block_id(self):
        """Generate block identifier tuple for the cell"""
        
        block_valuemap = {1: [0,1,2], 
                          2: [3,4,5],
                          3: [6,7,8],
                          }    

        for idx, num_list in block_valuemap.items():
            if self.pos_r in num_list:
                block_r = idx
            if self.pos_c in num_list:
                block_c = idx

        return (block_r, block_c)
    
    def fix_value(self, value):
        """Fix cell value to be the given input"""

        self.num_list = [value]

    def elim_num_from_cell(self, num):
        """Eliminate number from a cell's list"""

        if num in self.num_list:
            self.num_list.remove(num)

class BoardStateUpdater:
    """Calculates board states"""

    def __init__(self, board):
        self.all_cells = board.all_cells
    
    def init_board_state(self, initial_board_state):
        """Generate list of known cells based on initial board state"""

        known_cells_list = []
        for r_idx, row in enumerate(initial_board_state):
            for c_idx, num in enumerate(row):
                if num.isnumeric():
                    for cell in self.all_cells:
                        if cell.pos_r == r_idx and cell.pos_c == c_idx:
                            cell.fix_value(int(num))
                            known_cells_list.append(cell)        

        return known_cells_list

    def remove_num_by_known_cell(self, known_cell, all_cells):
        """Based on known cell value remove number from corresponding row/column/block cells"""

        for cell in all_cells:
            if cell is not known_cell:
                if cell.pos_r == known_cell.pos_r:
                    cell.elim_num_from_cell(known_cell.num_list[0])
                elif cell.pos_c == known_cell.pos_c:
                    cell.elim_num_from_cell(known_cell.num_list[0])
                elif cell.block == known_cell.block:
                    cell.elim_num_from_cell(known_cell.num_list[0])

    def fix_cells_by_exclusion(self):
        """check for a number in only one cell of a row/column/block and fix it"""

        for idx in range(9):
            cell_list_to_check = [*self.make_group_of_cells(idx)]
            for check_num in range(9):
                for cell_list in cell_list_to_check:
                    self.check_if_only_one(cell_list, check_num)

    def create_newly_fixed_cell_list(self, currently_known_cell_list):
        """Create a list of cells which value was fixed in this iteration cycle"""

        newly_known_cell_list = []
        for cell in self.all_cells:
            if len(cell.num_list) == 1:
                if cell not in currently_known_cell_list:
                    newly_known_cell_list.append(cell)

        return newly_known_cell_list 

    def new_board_state_calculator(self, currently_known_cell_list):
        """Modify other cell paramters based on newly known cells, and return with a list of brand new known cells"""

        for known_cell in currently_known_cell_list:
            self.remove_num_by_known_cell(known_cell, self.all_cells)
        self.fix_cells_by_exclusion() 

    def make_group_of_cells(self, idx):
        """Makes a list of cells with the same row/column/block index"""

        cell_list_r, cell_list_c, cell_list_b = [], [], []
        for cell in self.all_cells:
            if cell.pos_r == idx:
                cell_list_r.append(cell)
            if cell.pos_c == idx:
                cell_list_c.append(cell)
            if cell.pos_r == idx:
                cell_list_b.append(cell)
        
        return cell_list_r, cell_list_c, cell_list_b

    def check_if_only_one(self, cell_list, num):
        """Check from the list of cells if only one cell contain num and fix that value for the cell"""

        ctr = 0
        for cell in cell_list:
            if num in cell.num_list:
                marked_cell = cell
                ctr += 1
            if ctr > 1:
                break
        if ctr == 1:
            marked_cell.fix_value(num)

    def board_state_provider(self, current_board_state):
        """Transform the current board state cell list to a data structure for the plotter"""
        
        board_state_to_print = [[' ' for row in range(9)] for col in range(9)]

        for cell in current_board_state.all_cells:
            if len(cell.num_list) == 1:
                board_state_to_print[cell.pos_r][cell.pos_c] = f'{cell.num_list[0]}'
        
        return board_state_to_print


if __name__ == '__main__':
    
    from pprint import pprint

    board = Board()
    updater = BoardStateUpdater(board)

    board_list = [
        ['5', '4', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', '1', '4', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '2', '4'], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1'],
    ]
    
    known_cells = updater.init_board_state(board_list)
    pprint(known_cells)

    updater.new_board_state_calculator(known_cells)
    new_known_cell_list = updater.create_newly_fixed_cell_list(known_cells)
    pprint(new_known_cell_list)

    new_board_state = updater.board_state_provider(board)
    pprint(new_board_state)

    