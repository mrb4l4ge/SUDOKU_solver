class InputParser:
    """Parse the input file for known cells"""

    def __init__(self):
        self.init_board_state = []

    def read_input(self, input_file):
        """Read input file and parse it"""
        
        try:
            with open(input_file, 'r') as inputfile:
                for idx, line in enumerate(inputfile.readlines()):
                    self.check_line_validity(idx, line)
                    upd_line = list(map(lambda x: ' ' if x == '0' else x, line.split()))       # zeros in input file should be empty spaces in plot table
                    self.init_board_state.append(upd_line)
        except FileNotFoundError:
            print("Input file not found in working directory.")

        return self.init_board_state

    def check_line_validity(self, idx, line):
        """Check if the input file contain information in the right format."""

        line_list = line.split()
        if len(line_list) != 9:
            raise IndexError(f"Each line should contain exactly 9 numbers. Error found in line {idx+1}.")
        for num in line_list:
            if not num.isdigit():
                raise TypeError(f"Only positive integer numbers are allowed as cell values. Error found in line {idx+1} -> {num}") 
            if int(num) < 0 or int(num) > 9:
                raise ValueError(f"Only integers numbers between 0-9 are allowed (0 meaning blank cell). Error found in line {idx+1} -> {num}")
        

if __name__=='__main__':

    input_parser = InputParser() 
    init_board = input_parser.read_input('input_board.txt')
    print(init_board)