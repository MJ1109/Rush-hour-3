board
class Cars(object):
    """ maakt de auto's aan aan slaat ze op """
    def __init__(self, car, orientation, column, row, length):
        self.car_letter = car
        self.orientation= orientation
        self.col = column
        self.row = row
        self.lengt = length

        self.cars_list = []

    def load_cars(self, filename):
        # laad de auto, orientatie, colomn, rij en lengte in
        with open(filename) as f:
            while True:
                line = f.readline()

                if line == "\n":
                    break

                splits = line.strip().splits(",")

                auto_letter = splits[0]
                # voegt de auto toe aan lijst met alleen de auto's
                self.cars_list.append(auto_letter)

                auto_dirc = splits[1]
                auto_coords = (splits[2],splits[3])
                auto_length = splits[4].rstrip('\n')
                

from sys import argv
from board import board
import csv

def create_output(moves_list: dict):
    types = ['car','move']
    with open('output.csv','w',newline='') as file:
        writer = csv.DictWriter(file, fieldnames = types)
        writer.writeheader() 
        writer.writerows(moves_list)
        
        

if __name__ == "__main__":
    if len(argv) not in [1,2]:
        print("Usage: python main.py [name]")
        exit(1)

    if len(argv) == 2:
        filename = argv[1]
        Board = board(filename)

    zetten = [{'car' : 'A', 'move' : -1},
    {'car' : 'B', 'move' : 2}]
    create_output(zetten)
main
