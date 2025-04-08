
from input_parser import InputParser
from plotter import Plotter
from solver import *



if __name__ == '__main__':
    
    input_parser = InputParser() 
    plotter = Plotter() 
    init_board = input_parser.read_input('input_board.txt')
    plotter.plot_board(init_board)

    board = Board()
    board_updater = BoardStateUpdater(board)

    new_known_cells = board_updater.init_board_state(init_board)

    while True:
        
        board_updater.calc_board_state(new_known_cells)
        
        upd_new_known_cells = board_updater.create_newly_fixed_cell_list(new_known_cells)
        
        plotter.plot_board(board_updater.provide_board_state(board))

        new_known_cells = upd_new_known_cells

        if len(new_known_cells) == 0:
            break
        
        
    