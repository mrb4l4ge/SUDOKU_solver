

class Solver:
    '''Calculates board states'''

    def __init__(self):

        '''Initial board setup. Fill board with numbers'''
        
        self.current_board_state = [[[num+1 for num in range(9)] for row in range(9)] for col in range(9)]
        
        self.block_valuemap = {1: [0,1,2],
                               2: [3,4,5],
                               3: [6,7,8],
                               }


    def elim_num_from_row(self, row, num):
        '''Eliminate invalid number in all cells of a row'''
        
        for col in range(9):
            if num in self.current_board_state[row][col]:
                self.current_board_state[row][col].remove(num)
            

    def elim_num_from_col(self, col, num):
        '''Eliminate invalid number in all cells of a column'''
        
        for row in range(9):
            if num in self.current_board_state[row][col]:
                self.current_board_state[row][col].remove(num)

    def elim_num_from_block(self, row, col, num):
        '''Eliminate invalid number in all cells of a block'''

        for num_list in self.block_valuemap.values():
            if row in num_list:
                row_numlist = num_list
            if col in num_list:
                col_numlist = num_list

        for rownum in row_numlist:
            for colnum in col_numlist:
                if num in self.current_board_state[rownum][colnum]:
                    self.current_board_state[rownum][colnum].remove(num)

    def elim_num_from_board_spaces(self, row, col, num):
        '''Eliminate invalid number in all cells of rows, columns, blocks'''

        self.elim_num_from_row(row, num)
        self.elim_num_from_col(col, num)
        self.elim_num_from_block(row, col, num)

    def calc_row(self, row):
        '''Checks if only one cell contain a number in a row'''
        pass

    def calc_column(self, column):
        '''Checks if only one cell contain a number in a column'''
        pass

    def calc_block(self, block):
        '''Checks if only one cell contain a number in a block'''
        pass

    def fix_cell(self, block):
        '''Checks if only one number left in a cell'''
        pass


if __name__ == '__main__':
    
    from pprint import pprint

    # current_board_state = [[[num+1 for num in range(9)] for row in range(9)] for col in range(9)]
    # pprint(current_board_state)
    
    sol = Solver()
    sol.elim_num_from_board_spaces(0,1,5)
    pprint(sol.current_board_state)

    