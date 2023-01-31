from math import sqrt
import time
from board import Board
from cars import Cars 
import copy

# weights van de keuze af laten hangen van heuristieken, 
# bijv hoeveel auto's blokkeren de rode/hoeveel tegels tot uitgang

class Beam_search():
    '''
    calculates a path to the winning state
    width: the width of the beam
    return: a winning path if sulion is found, or nothing
    '''

    # take inputs
    def __init__(self,filename) -> None:
        
        self.filename = filename 
        self.fn = "gameboards/{filename}"
        self.board = Board(filename) 
        self.board.load_cars()
        self.board.in_position()
        self.board.generate_board()

    def beam(self):
        st = time.time()

        list_dir = [-1,1]
        
        self.board.print_board()
        
        amnt_steps = 0
        move = (0,0)

    
    def weight_calc(self, board):
        print(vars(board))
        obstructions = 0

        for car in board.cars:
            print(vars(car))
            if car.car_letter == 'X':
                y = car.row
                x = car.col

                for position in board.board[y][x+2:]:
                    if position != ' ':
                        obstructions += 1
        return obstructions

if __name__ == "__main__":
    beamsearch = Beam_search("Rushhour6x6_1.csv")
    board_copy= copy.deepcopy(beamsearch.board)
    beamsearch.weight_calc(board_copy, "A", -1)
   

