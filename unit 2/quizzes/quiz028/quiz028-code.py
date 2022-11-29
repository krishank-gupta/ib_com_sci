# import matplotlib for graphs as plt
from matplotlib import pyplot as plt

# init style
plt.style.use('ggplot')
plt.title("X over Y")
plt.xlabel("X")
plt.ylabel("Y")

# create x and y lists for graph
x_list = []
y_list = []
data = {
    'x': [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
    'y': [24,1,2,25,26,21,23,34,49,2,19,32,7,17,36,7,45,28,40,46],
    'title': "quiz028"
}

# for every number in interval: -10 < x < 10 
for i in range(len(data['x'])):
    # append i to x list
    x_list.append(data['x'][i])
    # calc y and append to y list
    y_list.append(data['y'][i])

# show graph
plt.plot(x_list, y_list, color='r')
plt.show()

