
from input_parser import InputParser
from plotter import Plotter
from solver import *

WELCOME_TEXT = """
Hello. 
This a SUDOKU solver program. It uses an 'input_board.txt' as an input file with a given format representing a Sudoku problem. 
The program tries to automatically solving the given problem and provide the solution.
Please, read the README file for further instructions.

Press 'y' key to continue or else to abort...
"""

def board_filled(board_state):
    """Check if board is completely filled"""

    filled_board = True
    for rows in board_state:
        if ' ' in rows:
            filled_board = False
            break
    return filled_board

if __name__ == '__main__':
    
    pressed_key = input(WELCOME_TEXT)
    if pressed_key.lower() == 'y':
        
        input_parser = InputParser() 
        plotter = Plotter() 
        init_board = input_parser.read_input('input_board.txt')
        plotter.plot_board(init_board)

        board = Board()
        board_updater = BoardStateUpdater(board)

        new_known_cells = board.init_board_state(init_board)

        while True:
            
            board_updater.calc_board_state(new_known_cells)
            upd_new_known_cells = board_updater.create_newly_fixed_cell_list(new_known_cells)
            curr_board_state = board.provide_board_state(board)  
            plotter.plot_board(curr_board_state)
            new_known_cells = upd_new_known_cells

            if board_filled(curr_board_state):
                break
        
        
        
    