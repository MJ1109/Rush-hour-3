from sys import argv
from board import board
import csv

def create_output():
    with open('output.csv','w',newline='') as file:
        writer = csv.writer(file)
        writer.writerow("car","move")
        

if __name__ == "__main__":
    if len(argv) not in [1,2]:
        print("Usage: python main.py [name]")
        exit(1)

    if len(argv) == 2:
        filename = argv[1]
        Board = board(filename)

    