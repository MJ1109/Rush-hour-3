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