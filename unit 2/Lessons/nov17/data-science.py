import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

h=[57.0, 56.0, 57.0, 56.0, 55.0, 55.0, 54.0, 54.0, 54.0, 53.0, 53.0, 54.0, 53.0, 53.0, 52.0, 52.0, 51.0, 51.0, 51.0] 
low=[53.0, 54.0, 54.0, 52.0, 54.0, 51.0, 53.0, 53.0, 50.0, 51.0, 52.0, 53.0, 49.0, 50.0, 50.0, 49.0, 50.0, 47.0, 50.0]
high= [58.0, 60.0, 61.0, 57.0, 56.0, 58.0, 58.0, 57.0, 56.0, 55.0, 54.0, 57.0, 54.0, 56.0, 53.0, 56.0, 53.0, 55.0, 52.0]


samples = []
for i in range(len(h)):
    samples.append(i)

fig = plt.figure(figsize=(8,4))

plt.subplot(1, 2, 1)
plt.plot(samples, h, color="#264653")
plt.plot(samples, low, color="#e76f51")
plt.plot(samples, high, color="#2a9d8f")

#Step3: Analyze data
mean = []
standar_deviation = []

for i in range(len(h)):
    data = [h[i], low[i], high[i]]
    mean.append(np.mean(data))
    standar_deviation.append(np.std(data))

plt.subplot(1,2,2)
plt.fill_between( samples, high, low, alpha = .5, linewidth = 0, color = "#264653" )
plt.errorbar(samples, mean, standar_deviation, fmt = "o", color = "#e76f51")
plt.title("Samples Over Mean with Error Bars")
plt.xlabel("Samples")
plt.ylabel("Mean")

plt.show()