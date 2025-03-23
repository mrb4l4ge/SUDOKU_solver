class InputParser:
    '''Parse the input file for known cells'''

    def __init__(self):
        self.init_board_state = []

    def read_input(self, input_file):
        '''Read input file and parse it'''
        
        with open(input_file, 'r') as inputfile:
            for line in inputfile.readlines():
                upd_line = list(map(lambda x: ' ' if x == '0' else x, line.split()))       # zeros in input file should be empty spaces in plot table
                self.init_board_state.append(upd_line)
        
        return self.init_board_state

if __name__=='__main__':

    input_parser = InputParser() 
    init_board = input_parser.read_input('input_board.txt')
    print(init_board)