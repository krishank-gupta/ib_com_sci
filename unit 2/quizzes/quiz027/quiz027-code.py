# matplotlib library for graphing
import matplotlib.pyplot as plt
# numpy for mean and standard deviation calculation
import numpy as np

# Graph setup: theme, size, title, axis labels
plt.style.use('ggplot')
# fig = plt.figure(figsize=(8,4))
plt.figure(figsize=(8,4))
plt.title("Samples Over Mean with Error Bars")
plt.xlabel("Samples")
plt.ylabel("Mean")

# Data from the quiz
sensorA=[16,24,24,9,23,26,26,23,25,14] 
sensorB=[2,19,25,10,11,24,17,7,24,17]
sensorC= [15,11,24,21,6,2,18,27,1,16]

# Init empty list for x vals
samples = []

# Append x vals to samples
for i in range(len(sensorA)):
    samples.append(i)

# Init mean, standard deviations, max, and min lists, will append values to these in a loop later
mean = []
standard_deviation = []
maxVal = []
minVal = []

# Loop for every value in any of the 3 data lists
for i in range(len(sensorA)):
    # Data is the term i of all 3 data lists
    data = [sensorA[i], sensorB[i], sensorC[i]]
    
    # calc mean,max,min,standard deviation and append to respective list from the data
    mean.append(np.mean(data))
    maxVal.append(max(data))
    minVal.append(min(data))
    standard_deviation.append(np.std(data))

# Show errorbar graph 
plt.errorbar(samples, mean, standard_deviation, fmt = "o", color = "#e76f51")
# Show fill min and max graph
plt.fill_between( samples, maxVal, minVal, alpha = .5, linewidth = 0, color = "#264653" )

# Display graph
plt.show()