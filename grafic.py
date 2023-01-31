import matplotlib.pyplot as plt
import numpy as np
import pandas as pd  
from baseline import Baseline
import csv 


# repeats the random algorithms how many times you ask it to
def repeat(input):

    # puts the counter for how may steps it took to solve it at 0
    Total_count = 0

    # makes a empty list 
    list = []
    list_csv = []
    list_time = []
    
    # ask how many times you want to solve rush hour 
    int_input = int(float(input))

    # excutes the loop 
    for i in range(int_input):
        
        base = Baseline("Rushhour6x6_2.csv") 
        
        # how many moves it took to solve 
        amount_s, final_r = base.algo()
        
        # puts every random solution in the list
        list.append(amount_s)
        list_csv.append(str(amount_s))
        list_time.append(final_r)

        # adds all the solutions to a total
        Total_count = Total_count + amount_s
    
    # gives the max value of the list
    maxValue = max(list)

    # gives the min value of a list 
    minValue = min(list)
   
   
    mean(int_input, Total_count)
    return int_input, Total_count, amount_s, maxValue, minValue, list, list_time, list_csv

# calculates the mean of random moves it takes to solve rushhour 
def mean(i_i, c):
    mean = c // i_i
    return mean 


# makes a boxplot
def box_plot(ma): 
    # data is the list of movements it took the complete rushhour  
    data = l 
    plt.boxplot(data)
    plt.title("Rushhour oplossingen")
    plt.yticks(np.arange(0, ma, 250))
    plt.xlabel(f"{i_input}x het algoritme opnieuw uitgevoerd")
    plt.savefig('box_plot.png')

    return plt.show()

# makes a scatterplot
def scatter_plot(l):
    count_list = []
    counter = 0 
    for counter in range(i_input):
        count_list.append(counter)

    # x-as is the list of movements it took the complete rushhour   
    x = l
    y = count_list

    plt.scatter(y,x)
    plt.axhline(mean)
    plt.title("Rushhour oplossingen")
    plt.ylabel("Hoeveel zetten om rushhour op te lossen")
    plt.xlabel("Ronde")
    plt.savefig('scatter_plot.png')
    return plt.show()

# makes a histogram 
def histogram(l):

    # x-as is the list of movements it took the complete rushhour  
    x = l
    plt.hist(x)
    plt.title("Rushhour oplossingen")
    plt.xlabel("Hoeveel zetten om rushhour op te lossen")
    plt.ylabel("Frequentie")
    plt.savefig('histogram.png')
    return plt.show()

# makes a line chart from the time it took to solve rushhour 
def time_LineChart(l_t):
    count_list = []
    counter = 0 
    for counter in range(i_input):
        count_list.append(counter)
    
    y_as = l_t
    x_as = count_list
    plt.plot(x_as, y_as)
    plt.title("Rushhour oplossingen")
    plt.xlabel("Tijd in milliseconden")
    plt.ylabel("Rondes")
    plt.savefig('time_LineChart.png')
    return plt.show()

# makes a csv file from the data 
def make_csv(l_c):
    header = ['moves to solution']
    data = l_c

    with open('random.csv', 'w', newline ='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(header)
        csv_writer.writerows(data)
    
    return None 

if __name__ == "__main__":
    input = input("How many rounds? ")
    i_input, Total_c, a_s, ma, mi, l, l_t, l_c = repeat(input)
    mean = mean(i_input, Total_c)
    
    
  
    

