import matplotlib.pyplot as plt
import numpy as np
import requests

plt.style.use('ggplot')


response = requests.get("http://192.168.6.142/readings")

data = response.json()
data = data['readings'][0]

samplesHum = []
sampleTemp = []
tempList = []
humList = []

for i in range(0, len(data),1):

    if data[i]['sensor_id'] == 1:
        tempList.append(data[i]['value'])
        sampleTemp.append(i)
    else:
        samplesHum.append(i)
        humList.append(data[i]['value'])


plt.figure(figsize=(8,4))

plt.subplot(1, 2, 1)
plt.plot(samplesHum, humList, color="#264653")
plt.title("Samples over Humidity")
plt.xlabel("Samples")
plt.ylabel("Humidity")

plt.subplot(1, 2, 2)
plt.plot(sampleTemp, tempList, color="#264653")
plt.title("Samples over Temperature")
plt.xlabel("Samples")
plt.ylabel("Temperature")

plt.show()