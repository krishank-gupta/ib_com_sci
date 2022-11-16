from matplotlib import pyplot as plt

plt.style.use('ggplot')

import random 

random.seed(1234)

def produce(n,m,s):
    print(f"| {'x'.center(10)} | {'y(x)'.center(10)} |")
    
    n = int(n)
    m = int(m)
    s = int(s)
    
    x_list = []
    y_list = []
    
    for i in range(n):

        x = random.randint(0,100)
        x_list.append(x)
    
        y = round(x ** ((1/2)*((m/s)**2)),2)
        y_list.append(y)

        print(f"| {str(x).center(10)} | {(str(y)).center(10)} |")

    return y_list, x_list


data_y, data_x = produce(10,5,2)

plt.plot(data_x, data_y, color='r')
plt.show()