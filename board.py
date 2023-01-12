class Board(object):
    """ maakt een board aan"""
    def __init__(self):
        self.board  = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

    def printboard(self):
        for row in (0,8):
            for column in (0,8):
                if row == 0:
                    print("1")
                elif self.board[row][column] == [row][0]:
                    print("1")
                elif self.board[row][column] == [row][7]:
                    print("1")
                else:
                     print("0")
                     



        
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
                
