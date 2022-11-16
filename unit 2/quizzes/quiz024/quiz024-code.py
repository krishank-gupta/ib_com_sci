from matplotlib import pyplot as plt

plt.style.use('ggplot')

x_list = []
y_list = []

for i in range(-10, 10+1, 1):
    x_list.append(i)
    y_list.append( 2 * ((i+5) ** 2))
    print(f"x = {i} y = {2 * ((i+5) ** 2)}")

plt.plot(x_list, y_list, color='r')
plt.show()