from board import Board
from cars import Cars
import random as rd
from myqueue import Queue
import copy

def change(nested_list):
    tuple_list = [tuple(l) for l in nested_list]
    return tuple(tuple_list)

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

