from cars import Cars 

# Searches dimensions based on filename
def search_dimensions(filename):
    if filename[19] == "6":
        return 6
    elif filename[19] == "9":
        return 9
    elif filename[19] == "1":
        return 12


class Board():
    """ maakt een board aan"""
    def __init__(self,filename) -> None:
        self.filename = filename
        self.cars = []
        self.dim = search_dimensions(filename)
        self.board = [[ ' ' for i in range(self.dim)] for j in range(self.dim)]

    def load_cars(self,filename):
        # open file and skip the first line
        with open(filename) as f:
            next(f)
            while True:
                
                line = f.readline()
                
                if line == '':
                    break

                info = line.split(',')
                length = int(info[4].rstrip('\n'))
                car = Cars(info[0],info[1],int(info[2]),int(info[3]),length)
                self.cars.append(car)
            f.close()  

    def generate_board(self):
        # Insert cars in their start position
        for car in self.cars:
            x = car.col - 1
            y = car.row - 1
            
            # Check orientation
            if car.orientation == 'H':       
                for i in range(car.length):
                    self.board[y][x + i] = car.car_letter

            else:
                for i in range(car.length):
                    self.board[y + i][x] = car.car_letter
                
        return print(*self.board, sep="\n")  

     # Check if Red car is in end position
    def is_solved(self):
        for car in self.cars:
            if car.car_letter == "X" and car.col == (self.dim - 2):
                return True
        return False
    
    ###def print_empty_board(self):
        for row in range(6):
            for column in range(6):
                print(f" {self.board[row][column]} ", end='')
            print()


    ###def add_cars(self):
        for i in range(Cars.cars_list):
            r = Cars.row
            c = Cars.col
            if Cars.orientation == "H":
                for i in range(Cars.length):
                   self.board[r][c + i] = Cars.letter
                   
            else:
                for i in range(Cars.length):
                    self.board[r+i][c] = Cars.letter

        return self.board    
                 

                
#if __name__ == '__main__':
#    from sys import argv

#    board1 = Board()
#   print(board1.print_empty_board())
#  print(board1.add_cars())

