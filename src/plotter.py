class Plotter:
    '''Plot current board'''

    def plot_board(self, board_list):
        '''Plot current state of the full board'''

        print('  === === ===  === === ===  === === ===  ')

        for idx, row_list in enumerate(board_list):
            print('|| {} | {} | {} || {} | {} | {} || {} | {} | {} ||'.format(*row_list))
            if (idx+1) % 3 == 0:
               print('  === === ===  === === ===  === === ===  ')
            else:
               print('  --- --- ---  --- --- ---  --- --- ---  ')
        
if __name__=='__main__':

    board = [
        [0,1,2,3,' ',5,6,7,8],
        [0,1,2,3,4,5,6,7,8],
        [0,1,2,3,4,5,6,7,8],
        [0,1,2,3,4,5,6,7,8],
        [0,1,2,3,4,5,6,7,8],
        [0,' ',2,3,4,5,6,7,8],
        [0,1,2,3,4,5,6,7,8],
        [0,1,2,3,4,5,6,8,8],
        [1,1,2,3,4,5,6,' ',8],
    ]
    plotter = Plotter() 
    init_board = plotter.plot_board(board)






