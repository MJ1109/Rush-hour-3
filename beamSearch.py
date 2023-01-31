from math import sqrt
from board import Board
from cars import Cars 

# weights van de keuze af laten hangen van heuristieken, 
# bijv hoeveel auto's blokkeren de rode/hoeveel tegels tot uitgang

class Beam_search():
    '''
    calculates a path to the winning state
    width: the width of the beam
    return: a winning path if sulion is found, or nothing
    '''

    # take inputs
    def __init__(self, filename) -> None:
        self.filename = filename 
        self.fn = "gameboards/{filename}"
        self.board = Board(filename) 
        self.board.load_cars()
        self.cars = Cars(car_letter, orientation, column, row, length)
    
    def weight_calc(self, filename):
        # calculate the cars that are blocking the exit
        # width = Board.search_dimensions(filename)
        # list_len = sqrt(len(Board.convert_string()))
        obstructions = 0

        

        for car in self.cars:
            x = car.col
            y = car.row

            while self.board[x + 1][y] < Board.dim:
                if car.car_letter == "X" and Board.board[y][x + 1] !=' ':
                    obstructions = obstructions + 1
                    x = x + 1
            return x

if __name__ == "__main__":
    beamsearch = Beam_search("Rushhour6x6_1.csv")
    print(beamsearch.weight_calc("Rushhour6x6_1.csv"))

    # def algorithm(self):
    #     list_dir = [-1,1]
    #     self.board.in_position()
    #     self.board.generate_board()
        
    #     steps = 0
    #     states = (0,0)


    #     while self.board.is_solved() == False:
    #         # self.board.generate_board()
    #         steps += 1
    #         states += 1
