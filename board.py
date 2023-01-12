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
                     