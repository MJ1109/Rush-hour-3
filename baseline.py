from board import Board
import random as rd

class Baseline():

    def __init__(self,filename) -> None:
        self.filename = filename 
        self.fn = "gameboards/{filename}"
        self.board = Board(filename) 
        self.board.load_cars()

    def algo(self):
        list_dir = [-1,1]
        self.board.in_position()
        self.board.generate_board()
        
        amnt_steps = 0
        move = (0,0)

        while self.board.is_solved() != True :
            dir = rd.choice(list_dir)
            r_car = rd.choice(self.board.cars)
                
            if move != (r_car,dir) and self.board.move(r_car.car_letter,dir) == True :
                self.board.move(r_car.car_letter,dir)
                move = (r_car.car_letter,dir)
                self.board.generate_board()
                amnt_steps += 1
            
        
        for car in self.board.cars:
            print(car.car_letter,car.moved)

        return amnt_steps
    

def print_results():
    base = Baseline("Rushhour6x6_1.csv")
    return print(base.algo())

print_results()