from board import Board
from cars import Cars
import random as rd
from queue_1 import Queue
from collections import deque
import copy


def convert(value):
    if value == -1:
        return 1
    if value == 1:
        return -1

def poss_moves(board):
    poss_moves = []
    dir = [-1,1]
    
    for car in board.cars:
        for i in dir:
            if board.possible_moves(car.car_letter,i) == True:
                poss_moves.append((car.car_letter,i))
   
    return poss_moves

def child_states(board):
    pss = poss_moves(board)
    child_state = []
    poss = rd.sample(pss, k = len(pss))
    for p in poss:
        c = board.move(p[0],p[1])
        c.generate_board()
        child_state.append(c)
    
    print(child_state)
    return child_state

class Breadth_first():

    def __init__(self,filename,max_depth) -> None:
        self.filename = filename 
        self.board = copy.deepcopy(Board(self.filename))
        self.board.load_cars()
        #self.board.in_position()
        #self.board.generate_board()
        self.max_depth = max_depth
        self.solutions = []
    
    # Function that searches for child states
    def ss(self,board):
        possible = []
        board.generate_board()
        
        next_moves = board.can_move(board)
    
        for next in next_moves:
            new_cars = copy.deepcopy(board.cars)
            new = copy.deepcopy(board)
            d = new.move(next[0],next[1])
            new.generate_board()
            possible.append(d)
            

        return possible


    def poging_twee(self):
        queue = list()
        closed = dict()
        self.board.in_position()
        self.board.generate_board()
        closed[self.board.convert_string()] = None
        queue.append(self.board)
        begin = (0,0)
        path = []
        path.append(begin)


        
        while len(queue) != 0 :
            
            # get the first node from the queue
            current = queue.pop(0)
            current.generate_board() 
            cur_str = current.convert_string()
            
        
            # Check if solved        
            if current.is_solved() == True:
                print(len(closed))
                return current.print_board()
             

            posss = self.ss(current)
            # Search in child states if visited already
            for l in posss:
                self.board.cars = l.cars
                l.generate_board()
                new_board = l.convert_string()
            
                if new_board not in closed:
                    queue.append(l)
                    path.append(l)
                    closed[new_board] = cur_str
            
            
            
                


breadth = Breadth_first("Rushhour6x6_1.csv",100)
print(breadth.poging_twee())

