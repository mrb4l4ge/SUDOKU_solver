class InputParser:
    '''Parse the input file for known cells'''

    def __init__(self, input_file):
        self.input_file = input_file
        self.init_board_state = []

    def read_input(self):
        '''Read input file and parse it'''
        
        with open(self.input_file, 'r') as inputfile:
            for line in inputfile.readlines():
                self.init_board_state.append(line.split())
        
        return self.init_board_state

if __name__=='__main__':

    input_parser = InputParser('input_board.txt') 
    init_board = input_parser.read_input()
    print(init_board)