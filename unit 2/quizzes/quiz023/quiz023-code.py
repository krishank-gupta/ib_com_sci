# import matplotlib for graphing as plt
from matplotlib import pyplot as plt
# import random to create random numbers
import random 

# graph style initialization
plt.style.use('ggplot')
# Seed to start random number generation at 1234
random.seed(1234)

# main function that takes 3 parameters
def produce(n,m,s):
    # print the header
    print(f"| {'x'.center(10)} | {'y(x)'.center(10)} |")
    
    # List with x values for graph
    x_list = []
    # List with y values for graph
    y_list = []
    
    # for loop in range of param n
    for i in range(n):

        # generate random number between 0 and 100
        x = random.randint(0,100)
        # add x to the list of x values
        x_list.append(x)

        # calculate y
        y = round(x ** ((1/2)*((m/s)**2)),2)
        # add y to the list of y values
        y_list.append(y)

        # print x and y
        print(f"| {str(x).center(10)} | {(str(y)).center(10)} |")

    # return x and y lists for graph
    return y_list, x_list

# save output from function in two variables
data_y, data_x = produce(10,5,2)

# use above variables to show graph
plt.plot(data_x, data_y, color='r')
plt.show()