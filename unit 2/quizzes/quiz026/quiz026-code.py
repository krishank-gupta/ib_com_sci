
import matplotlib.pyplot as plt
import numpy as np


h = [57.0, 56.0, 57.0, 56.0, 55.0, 55.0, 54.0, 54.0, 54.0, 53.0, 53.0, 54.0, 53.0, 53.0, 52.0, 52.0, 51.0, 51.0, 51.0, 50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 48.0, 49.0, 49.0, 48.0, 48.0, 48.0, 49.0]

samples = []

for i in range(0, len(h), 1):
    samples.append(i)

plt.style.use('ggplot')

plt.title("Linear equation of relative humidity")
plt.xlabel("Samples")
plt.ylabel("Relative humidity")

m, b = np.polyfit(samples, h, 1)
print(f"Linear equation is y = {m:.2f}x + ({b:.2f})")

x_model = [1, 32]
y_model = []

for i in x_model:
    y_model.append(m * i + b)

plt.plot(samples,h, linestyle='none', marker="v")
plt.plot(x_model, y_model)

plt.show()