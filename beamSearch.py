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
        self.list = []
    
    def weight_calc(self, board, car, dir):
        # calculate the amount of cars obstructing the path of car X 
        print(vars(board))
        obstructions = 0

        for car in board.cars:
            # print(vars(car))
            if car.car_letter == 'X':
                y = car.row
                x = car.col

                for position in board.board[y][x+2:]:
                    if position != ' ':
                        obstructions += 1
        print(obstructions)
        return obstructions

    def empty_spot(self, board): 
        print("hoi")
        for y in board:
            for x in board:
                if board[y][x] == ' ':
                    list.append(board[y][x])
        
        print(list)

    # if 


if __name__ == "__main__":
    beamsearch = Beam_search("Rushhour6x6_1.csv")
    board_copy= copy.deepcopy(beamsearch.board)
    # beamsearch.weight_calc(board_copy, "X", -1)
    print(beamsearch.empty_spot(Board))
#   controleren welke moves mogelijk zijn
#   vergelijk welke moves de kleinste weights hebben
#   sla kleinste moves op *ergens* en uitvoeren
#   kijk vanaf die moves verder naar oplossing, als oplossing gevonden => won 
#       anders terug naar andere move om oplossing te vinden tot game = won 