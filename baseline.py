from board import Board
import random as rd
import time 

class Baseline():
   
    def __init__(self,filename) -> None:
        
        self.filename = filename 
        self.fn = "gameboards/{filename}"
        self.board = Board(filename) 
        self.board.load_cars()

    def algo(self):
        st = time.time()

        list_dir = [-1,1]
        self.board.in_position()
        self.board.generate_board()
        
        amnt_steps = 0
        move = (0,0)

        while self.board.is_solved() != True :
            dir = rd.choice(list_dir)
            r_car = rd.choice(self.board.cars)
                
            if move != (r_car,dir) and self.board.possible_moves(r_car.car_letter,dir) == True :
                self.board.move(r_car.car_letter,dir)
                move = (r_car.car_letter,dir)
                self.board.generate_board()
                amnt_steps += 1
       
        et = time.time()
        elapsed_time = et - st
        final_res = elapsed_time * 1000
       

        return amnt_steps, final_res
    
    def print_solutions(self):
        solutions = []

        for car in self.board.cars:
            solutions.append((car.car_letter,car.moved))
        
        return print(solutions)
    

def print_results(solutions):
    base = Baseline("Rushhour12x12_7.csv")
    print(base.algo())
    if solutions == True:
        return base.print_solutions()
   

if __name__ == "__main__":
    print_results(False)