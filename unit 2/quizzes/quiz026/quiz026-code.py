# Import matplotlib for graphing
import matplotlib.pyplot as plt
# Import numpy to calculate standard deviation
import numpy as np

# the data from the quiz
h = [57.0, 56.0, 57.0, 56.0, 55.0, 55.0, 54.0, 54.0, 54.0, 53.0, 53.0, 54.0, 53.0, 53.0, 52.0, 52.0, 51.0, 51.0, 51.0, 50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 48.0, 49.0, 49.0, 48.0, 48.0, 48.0, 49.0]

# x vals
samples = []

# For every inde in data
for i in range(0, len(h), 1):
    # Append index to x vals list
    samples.append(i)

# Graph setup
plt.style.use('ggplot')
plt.title("Linear equation of relative humidity")
plt.xlabel("Samples")
plt.ylabel("Relative humidity")

# Polyfit calc
m, b = np.polyfit(samples, h, 1)
print(f"Linear equation is y = {m:.2f}x + ({b:.2f})")

# data from 1 to 32
x_model = [1, 32]
y_model = []

# For the required data interval, calculate y using model mx+b 
for i in x_model:
    # Append y val to y_model list
    y_model.append(m * i + b)

# Plot graph
plt.plot(samples,h, linestyle='none', marker="v")
plt.plot(x_model, y_model)

# Show graph
plt.show()