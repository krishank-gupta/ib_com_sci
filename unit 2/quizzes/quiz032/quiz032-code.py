import matplotlib.pyplot as plt
import numpy as np
import requests

plt.style.use('ggplot')


response = requests.get("http://192.168.6.142/readings")

data = response.json()
data = data['readings'][0]

tempList = []
humList = []

for i in range(0, len(data),1):

    if data[i]['sensor_id'] == 9:
        tempList.append(data[i]['value'])
    elif data[i]['sensor_id'] == 10:
        humList.append(data[i]['value'])

# Calc data per hour
samplesPerHour = 12 # 1 sample per 5mins
tempHour = []
samples = []
humHour = []

for t in range(0, len(tempList), samplesPerHour):
    temp_a = tempList[t:t+samplesPerHour]
    tempHour.append(sum(temp_a)/len(temp_a))
    temp_b = humList[t:t+samplesPerHour]
    humHour.append(sum(temp_b)/len(temp_b))
    samples.append(t)

plt.figure(figsize=(10,6))
plt.subplot(3, 1, 1)
plt.plot(samples, tempHour, color="#264653")
plt.subplot(3, 1, 2)
plt.plot(samples, humHour, color="#264653")

# difference
differences = []
for i in range(len(tempHour)):
    differences.append(tempHour[i] - humHour[i])

plt.subplot(3,1,3)
plt.plot(samples,differences, color="#264653")

plt.show()
