from board import Board
import random as rd
import copy
import statistics
import time


class Breadth_first():

    def __init__(self,filename) -> None:
        self.filename = filename 
        self.board = copy.deepcopy(Board(self.filename))
        self.board.load_cars()
        self.queue = list()
        self.queue.append(self.board)
        self.visited = dict()
        self.path = []
        self.solutions = []
    
    # Function that searches for child states
    def ss(self,board):
        board.generate_board()
        
        next_moves = board.can_move(board)
        # For all possible moves create a child board
        for next in next_moves:
            new = copy.deepcopy(board)
            d = new.move(next[0],next[1])
            d.generate_board()

            # check if board has been visited
            if d.convert_string() in self.visited.keys():
                continue
            else:
                self.visited[d.convert_string()] = board.convert_string()
                self.queue.append(d)
                del(d)

        
    def poging_twee(self):
        self.board.in_position()
        self.board.generate_board()
        self.st_board_string = self.board.convert_string()
        self.visited[self.st_board_string] = 0
        self.solution_strings = []
        
        while len(self.queue) != 0 :
            
            # get the first node from the queue
            current = self.queue.pop(0)
            current.generate_board() 
            self.cur_str = current.convert_string()
            
            # Check if solved        
            if current.is_solved() == True:
                self.load_soluto(self.cur_str,current)
                amnt_sol = len(self.solution_strings)
                amnt_move = len(self.full_solutions(current))
                moves_made = self.full_solutions(current)
                return amnt_move,amnt_sol,moves_made
            
            self.ss(current)

    # Load solutions for board
    def load_soluto(self,parent,parent_board):
        
        while self.st_board_string not in self.solution_strings:
            self.solution_strings.append(parent)
            self.path.append(parent_board)
            self.load_soluto(self.visited[parent],parent_board)

    # 
    def full_solutions(self,board):
        moves = []
        for car in board.cars:
            moves.append((car.car_letter,car.moved))
        return moves
            
            

# Check how long it lasts
def time_algo():
    st = time.time()
    breadth = Breadth_first("Rushhour9x9_4.csv")
    breadth.poging_twee()
    et = time.time()
    elapsed = et-st 
    return elapsed

# Print average, min and max time
elp_tim = []
for i in range(1):
    print(i)
    elp_tim.append(time_algo())

print(min(elp_tim))
print(max(elp_tim))
print(statistics.mean(elp_tim))



