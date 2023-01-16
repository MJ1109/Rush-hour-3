from cars import Cars 
class Board(object):
    """ maakt een board aan"""
    def __init__(self):
        self.board  = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

    def print_empty_board(self):
        for row in range(6):
            for column in range(6):
                print(f" {self.board[row][column]} ", end='')
            print()

    def add_cars(self):
        for cars_list in Cars.cars_list:
            r = Cars.row
            c = Cars.col
            if Cars.orientation == "H":
                for i in range(Cars.length):
                    self.board[row][col + i] = Cars.letter
            else:
                for i in range(Cars.length):
                    self.board[row+i][col] = Cars.letter

        return self.board    
