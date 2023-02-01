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
        self.board = Board(self.filename)
        self.board.load_cars()
        self.board.in_position()
        self.board.generate_board()
        self.max_depth = max_depth
        self.solutions = []
    

    def poging_twee(self):
        queue = list()
        closed = dict()
        bb = copy.deepcopy(self.board)
        closed[self.board.convert_string()] = None
        queue.append(bb)
        begin = (0,0)
        path = []
        path.append(begin)


        while len(queue):
            #print(path)
            # get the first node from the queue
            node = queue.pop(0)
            node.generate_board()  
            fa = rd.sample(poss_moves(node), k = len(poss_moves(node)))
            print(len(queue))

            # generate all possible children

            for move in node.can_move():
                #print(move)
                child = node.move(move[0],move[1])
                new = child.generate_board()
                child.print_board()
                print()
                #child.generate_board()
                #print("node",node.convert_string())
                #print("child",new.convert_string())
                
                # check if child has already been processed
                
                if child.convert_string() not in closed:
                    # add child to closed list and to the queue
                    
                    print("wel gelukt:" , move)
                    closed[child.convert_string()] = [node.cars]
                    queue.append(child)
                    #print(child.convert_string())
                    path.append(1)
                else:
                    print(":(")
                # check if current child is a solution
                if child.is_solved():
                    return print(child.convert_string())
                


breadth = Breadth_first("Rushhour6x6_1.csv",100)
print(breadth.poging_twee())