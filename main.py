from sys import argv
import csv
from board import Board

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
        board = Board(filename)
        board.load_cars()
        position = board.in_position()
        board.generate_board()


    zetten = [{'car' : 'A', 'move' : -1},
    {'car' : 'B', 'move' : 2}]
    create_output(zetten)

    # auto_positie = board.cars_position()
    while board.is_solved() == False: 
        auto = input("auto die je wil schuiven: ")
        dirc = input("welke kant(-1 of 1)? ")
        valid = board.move(auto, dirc)
        board.generate_board()
        board.print_board()

    
    