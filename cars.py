from sys import argv
import csv 

class Cars():
    """ maakt de auto's aan aan slaat ze op """
    def __init__(self, car_letter, orientation, column, row, length):
        self.car_letter = car_letter
        self.orientation= orientation
        self.col = column
        self.row = row
        self.length = length
        self.moved = 0

    def has_moved(self, moves):
        self.moved = self.moved + moves
        return self.moved
    

    def __str__(self):
        return str(self.car_letter + self.orientation + self.col + self.row + self.length + self.moved)


   