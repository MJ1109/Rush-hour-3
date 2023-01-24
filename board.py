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
            x = car.col
            y = car.row
            
            # Check orientation
            if car.orientation == 'H' and x != 5:       
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
        
    def in_position(self):
        for car in self.cars:
            car.col = car.col - 1
            car.row = car.row - 1
    
    

    def move(self, auto): 
        # Move the cars if the space around them is empty
        for car in self.cars:
            if car.car_letter == auto: 
                x = car.col
                y = car.row
                
                # move left
                if car.orientation == 'H' and x -1 >= 0 and  self.board[y][x-1] == ' ':
                    x = x - 1 
                    self.board[y][x] = car.car_letter
                    self.board[y][x + car.length] = ' '
                    car.col = x 
                    return True
                
                # right
                elif car.orientation == 'H' and  x != 5 and self.board[y][x + car.length] == ' ':
                    x = x + car.length

                    self.board[y][x] = car.car_letter
                    self.board[y][x - car.length ] = ' '

                    if car.length == 2: 
                        car.col = x - 1 
                    else: 
                        car.col = x - 2
                    return True

                # up
                elif car.orientation == 'V' and  y - 1 >= 0 and self.board[y - 1][x] == ' ':
                    y = y - 1

                    self.board[y][x] = car.car_letter
                    self.board[y + car.length][x] = ' '

                    car.row = y
                        
                    return True
                
                # down
                elif car.orientation == 'V' and  y != 5 and self.board[y + car.length][x] == ' ':
                    y = y + car.length

                    self.board[y][x] = car.car_letter
                    self.board[y - car.length][x] = ' '
                    
                    if car.length == 2: 
                        car.row = y - 1 
                    else: 
                        car.row = y - 2

                    return True
                    
               
