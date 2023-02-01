# from board import Board
# from priority_q import PriorityQueue
# import copy

# # class Best_First(board, heuristic):
# #     def __init__(self) -> None:
# #         self.queue = PriorityQueue()
# #         self.moves = 0
# #         self.states = 0
# #         self.board = Board()
# #         self.cars = list(Board.load_cars)
# #         self.queue.push([self.moves, self.cars], 0)

# #     while self.board.is_solved(cars) != True:
        
# def best_first(board, heurstic):
#     queue = PriorityQueue
#     moves = 0
#     states = 0
#     board = Board("Rushhour6x6_1.csv")
#     cars = list(board.load_cars())
    

#     queue.push([moves, cars], 0)
    

#     while board.is_solved != True:
#         moves, cars = queue.get_priority()
#         board.generate_board(cars)
#         moves_list = []
#         moves_list.append(board.move(cars.car))
#         moves += 1
#         states += 1
#         print(moves)

# if __name__ == "__main__":        
#     best_first("Rushhour6x6_1.csv", "idkyet")


""" Module containing Best First algorithm to solve Rush Hour. Contains a
function best_first, which solves a Rush Hour game using breadth first search
combined with a heuristic of choice.
"""
from board import Board
from priority_q import PriorityQueue
from cars import Cars


def best_first(game, heuristic):
    """ Create priority queue for all child fields of Rush Hour board, get first
    in first out. Check if field is unique, then call heuristic and append to queue.
    Heuristic 'cars to exit' counts the number of cars blocking the red car to the exit.
    Hueristic 'cars in traffic' counts the number of cars to move, before the
    red car can be moved.
    Return number of moves needed to solve the game and number of states checked.
    Keyword arguments:
    game -- RushHour object
    heuristic -- string containing heuristic to apply
    """
    queue = PriorityQueue()
    moves = 0
    states = 0
    board = Board()
    cars = Cars()
    vehicles = list(board.load_cars())
    queue.push([moves, vehicles], 0)

    # def child_fields

    while not board.is_solved(cars):
        moves, vehicles = queue.get_priority()
        board.generate_board(vehicles)
        child_fields = game.get_child_fields_whole_step(vehicles)
        moves += 1
        states += 1
        print(moves)
        for field in child_fields:
            if game.is_unique(field):
                if heuristic == "cars_to_exit":
                    priority = moves + game.cars_to_exit(field)
                elif heuristic == "cars_in_traffic":
                    priority = moves + game.cars_in_traffic(field)
                queue.push([moves, field], priority)
    
    print(moves)
    print(states)
    return moves, states
