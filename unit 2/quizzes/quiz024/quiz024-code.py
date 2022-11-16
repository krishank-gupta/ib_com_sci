# import matplotlib for graphing as plt
from matplotlib import pyplot as plt

# set style of graph
plt.style.use('ggplot')

# create x and y lists for showing graph
x_list = []
y_list = []

# for every number in interval: -10 < x < 10 
for i in range(-10, 10+1, 1):
    # append i to list of x values
    x_list.append(i)
    # calc y and append to list of y values
    y_list.append( 2 * ((i+5) ** 2))

    # print x and y
    print(f"x = {i} y = {2 * ((i+5) ** 2)}")

# use the x and y list to show graph
plt.plot(x_list, y_list, color='r')
plt.show()