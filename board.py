class Board(object):
    """ maakt een board aan"""
    def __init__(self):
        self.board = [[1,1,1,1,1,1,1,1],[1,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1]]

    def print_empty_board(self):
        for row in range(8):
            for column in range(8):
                print(f" {self.board[row][column]} ", end='')
            print()
                     



        
        self.load_board(f"gameboards/{filename}.csv")
        
    def load_board(self,filename):

        with open(filename) as f:

            while True:
                line = f.readline()

                if line == "\n":
                    break

                auto_data = line.split(',')
                auto_letter = auto_data[0]
                auto_dirc = auto_data[1]
                auto_coords = (auto_data[2],auto_data[3])
                auto_length = auto_data[4].rstrip('\n')
                
