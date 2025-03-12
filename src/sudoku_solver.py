class InputParser:
    '''Parse the input file for known cells'''

    def __init__(self, input_file):
        self.input_file = input_file
        pass

    def read_input(self):
        '''Read input file and parse it'''
        pass
        # return newly_known_cells

class Plotter:
    '''Plot current board'''

    def __init__(self, board):
        self.board = board
        pass

    def plot_full_board(self):
        '''Plot current state of the full board'''
        pass

    def highlight_row(self):
        '''Highlight a certain row of the board'''
        pass

    def highlight_column(self):
        '''Highlight a certain column of the board'''
        pass

    def highlight_block(self):
        '''Highlight a certain block of the board'''
        pass

    def highlight_cell(self):
        '''Highlight a certain cell on the board'''
        pass

class Board:
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





# input board

# Fill cells with numbers

# Begin cycle:
# - Eliminate invalid numbers in cells based on previously filled numbers
#       - Eliminate rows, columns, block of the known number 
# - Calc known cells -> give back a list of them
#       - Check rows, columns, blocks
#       - If a cell is known, replot board with highlights
# - Repeat
# 