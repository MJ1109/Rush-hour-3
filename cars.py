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


    def __str__(self):
        return str(self.car_letter + self.orientation + self.col + self.row + self.length)


    # def load_cars(self, filename):
    #     # laad de auto, orientatie, colomn, rij en lengte in
    #     with open(filename) as f:
    #         while True:
    #             line = f.readline()

    #             if line == "\n":
    #                 break

    #             splits = line.strip().splits(",")

    #             car_letter = splits[0]
    #             # voegt de auto toe aan lijst met alleen de auto's
    #             self.list.append(car_letter)
    #             orientation = splits[1]
    #             col = splits[2]
    #             row = splits[3]
    #             lengt = splits[4]
    #             print(f"{self.cars_list}")

                # auto_dirc = splits[1]
                # auto_coords = (splits[2],splits[3])
                # auto_length = splits[4].rstrip('\n')

# if __name__ == '__main__':
#     car1 = Cars()
#     print(car1.load_cars())