import matplotlib.pyplot as plt
import numpy as np
import requests

response = requests.get("http://192.168.6.142/readings")
data = response.json()
data = data['readings'][0]

print(len(data))

temps = []

for i in data:
    if i['sensor_id'] == 1:
        temps.append(i['value'])

# Scatter plot in given window
temp_period = temps[610:800]
samples = []
for i in range(0, len(temp_period), 1):
    samples.append(i)

plt.scatter(samples, temp_period, color='red')


# Linear Equation
m,b = np.polyfit(samples, temp_period, 1)
x_line = [0, (800-610)]
y_line = []

for i in x_line:
    y_line.append(m*i+b)

plt.plot(x_line, y_line, color='#000000')

# Quadratic Equation
a1,a2,a3 = np.polyfit(samples, temp_period, 2)

y_line_quadratic = []
x_line_quadratic = []

for idx,i in enumerate(samples):
    y_line_quadratic.append(a1*(i**2) + a2*i + a3 )
    x_line_quadratic.append(idx)

plt.plot(x_line_quadratic, y_line_quadratic, 'red')

plt.show()