from board import Board
from cars import Cars
import random as rd
from queue_1 import Queue


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

class Breadth_first():

    def __init__(self,filename,max_depth) -> None:
        self.filename = filename 
        self.board = Board(self.filename)
        self.board.load_cars()
        self.max_depth = max_depth
        self.solutions = []

    def func_met_q(self):
        queue = list()
        new_path = Queue()
        self.board.in_position()
        self.board.generate_board()
        prev_move = (0,0)
        queue.append(self.board)
        new_path.enqueue(prev_move)
        closed = dict()
        closed[self.board] = None

        
        # Start while loop
        while len(queue) :

            # Haal eerste item uit queue
            node = queue.pop(0)
            new_path.dequeue()

            # Hossel de mogelijke moves
            poss_move = poss_moves(node)
            pss = rd.sample(poss_move,k = len(poss_move))

            # Voor alle mogelijke moves maak een child state
            for moves in pss:

                if prev_move != (moves[0],convert(moves[1])): 

                    # Beweeg het bord echt
                    node.move(moves[0],moves[1])
                    
                    node.generate_board()
                    #child = self.board.convert_string()
                    #cc = copy.deepcopy(cc)
                    prev_move = (moves[0],moves[1])
                    #print(moves)
                    # Maak een child state en sla de gemaakte moves op 
                    child = node.convert_string()
                    
                    new_path.enqueue((moves[0],moves[1]))
                   
                    # Controleer of we niet eerder deze zet hebben gemaakt
                    if child not in closed:
                        closed[child] = [node.cars,moves]
                        queue.append(node)
                        

                    # Check of is opgelost
                    
                    if node.is_solved() == True:
                        # check om te kijken of er oplossingen zijn
                        print("yes")
                        self.solutions.append(1)
                                                
                        return len(self.solutions)
    
    def __eq__(self,other) -> bool:
        return self.value == other.value


breadth = Breadth_first("Rushhour6x6_1.csv",100)
print(breadth.func_met_q())