# import matplotlib for graphs as plt
from matplotlib import pyplot as plt

# init style
plt.style.use('ggplot')

# create x and y lists for graph
x_list = []
y_list = []

# for every number in interval: -10 < x < 10 
for i in range(-10, 10+1, 1):
    # append i to x list
    x_list.append(i)
    # calc y and append to y list
    y_list.append(abs(i))

# show graph
plt.plot(x_list, y_list, color='r')
plt.show()