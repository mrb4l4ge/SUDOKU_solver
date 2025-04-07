
from input_parser import InputParser
from plotter import Plotter
from solver import Solver



if __name__ == '__main__':
    
    input_parser = InputParser() 
    init_board = input_parser.read_input('input_board.txt')

    plotter = Plotter() 
    init_board = plotter.plot_board(init_board)


# input board
    # instantiate inputParser
    # run reader method

# Fill cells with numbers
    # instantiate board state updater
        # run 'while' cycle until board is filled using class methods
        # Begin cycle:
        # - Eliminate invalid numbers in cells based on previously filled numbers
        #       - Eliminate rows, columns, block of the known number 
        # - Calc known cells -> give back a list of them
        #       - Check rows, columns, blocks
        #       - If a cell is known, replot board with highlights
        # - Repeat
        # 
    