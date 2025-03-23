

class Solver:
    '''Calculates board states'''

    def __init__(self):
        '''Initial board setup. Fill board with numbers.'''
        self.newly_known_cells = []
        self.known_cells = []
        pass

    def elim_row(self, row, num):
        '''Eliminate invalid number in all cells of a row'''
        pass

    def elim_column(self, column, num):
        '''Eliminate invalid number in all cells of a column'''
        pass

    def elim_block(self, block, num):
        '''Eliminate invalid number in all cells of a block'''
        pass

    def elim_board(self, row, column, block, num):
        '''Eliminate invalid number in all cells of rows, columns, blocks'''

        self.elim_row(row, num)
        self.elim_column(column, num)
        self.elim_block(block, num)

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
    pass

    