class Board:
    '''Represent the board made of 9x9 cells'''

    def __init__(self):
        self.board = self.setup_board()
    
    def setup_board(self):
        '''Setup the board frpom cell objects'''

        board = []
        for row in range(9):
            for col in range(9):
                self.board.append(Cell(row,col))

        return board

class Cell:
    '''Represent one cell in the board'''

    def __init__(self, pos_r, pos_c):
        self.pos_r = pos_r
        self.pos_c = pos_c
        self.num_list = [n+1 for n in range(9)]
        self.block = self.gen_blocks()

    def gen_blocks(self):
        '''Generate block identifier tuple for the cell'''
        
        block_valuemap = {1: [0,1,2], 
                          2: [3,4,5],
                          3: [6,7,8],
                          }    

        for num_list in block_valuemap.values():
            if self.pos_r in num_list:
                block_r = num_list
            if self.pos_c in num_list:
                block_c = num_list

        return (block_r, block_c)
    
    def fix_value(self, value):
        '''Fix cell value to be the given input'''

        self.num_list = [value]

    def elim_num_from_cell(self, num):
        '''Eliminate number from a cell's list'''

        if num in self.num_list:
            self.num_list.remove(num)

class BoardStateUpdater:
    '''Calculates board states'''

    def __init__(self, board):
        self.board = board
    
    def board_state_initiator(self, initial_board_state):
        '''Generate list of known cells based on initial board state'''

        known_cells_list = []
        for r_idx, row in enumerate(initial_board_state):
            for c_idx, num in enumerate(row):
                if num.isnumeric():
                    for cell in self.board:
                        if cell.pos_r == r_idx and cell.pos_c == c_idx:
                            cell.fix_value(num)
                            known_cells_list.append(cell)        

        return known_cells_list

    def new_board_state_calculator(self, newly_known_cell_list):
        '''Modify other cell paramters based on newly known cells, and return with a list of brand new known cells'''

        for known_cell in newly_known_cell_list:
            for cell in self.board:
                if cell.pos_r == known_cell.pos_r:
                    cell.elim_num_from_cell(known_cell.num_list[0])
                elif cell.pos_c == known_cell.pos_c:
                    cell.elim_num_from_cell(known_cell.num_list[0])
                elif cell.block == known_cell.block:
                    cell.elim_num_from_cell(known_cell.num_list[0])

        # check for a number in only one cell of a row/column/block and fix it

        updated_newly_known_cell_list = []

        for cell in self.board:
            if len(cell.num_list) == 1:
                if cell not in newly_known_cell_list:
                    updated_newly_known_cell_list.append(cell)

        return updated_newly_known_cell_list        
        

    def board_state_provider(self, current_board_state):
        '''Transform the current board state cell list to a data structure for the plotter'''
        
        board_state_to_print = [' ' for row in range(9) for col in range(9)]

        for cell in current_board_state:
            if len(cell.num_list) == 1:
                board_state_to_print[cell.pos_r][cell.pos_c] = f'{cell.num_list[0]}'
        
        return board_state_to_print


    


if __name__ == '__main__':
    
    from pprint import pprint

    # current_board_state = [[[num+1 for num in range(9)] for row in range(9)] for col in range(9)]
    # pprint(current_board_state)
    
    sol = Solver()
    sol.elim_num_from_board_spaces(0,1,5)
    pprint(sol.current_board_state)

    