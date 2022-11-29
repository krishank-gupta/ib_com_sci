import matplotlib.pyplot as plt
import numpy as np
import serial
import time

arduino = serial.Serial(port='/dev/cu.usbserial-1420', baudrate=9600, timeout=.1)

plt.style.use('ggplot')
plt.figure(figsize=(8,4))

def read():
    data = ""
    while len(data)<1:
        data = arduino.readline()
    return data

samples = []
humList = []
tempList = []

for i in range(0,10,1):
    time.sleep(0.1)
    value = read() #wait until data is in the port
    msg = value.decode('utf-8').split(' ')

    if len(msg) > 1:    
        samples.append(i)
        # print(msg[0].split(':')[1].replace('%',''))
        humList.append(msg[0].split(':')[1].replace('%','')) # use [0,-1] instead for %
        tempList.append(msg[1].split(':')[1].replace('C','').rstrip())
    

print(samples)
print(humList)
print(tempList)

m, b = np.polyfit(samples, humList, 1)
print(f"Linear equation is y = {m:.2f}x + ({b:.2f})")

plt.subplot(1, 2, 1)
plt.plot(samples, humList, color="#264653")
plt.title("Samples over humidity")
plt.xlabel("Samples")
plt.ylabel("Humidity")

plt.subplot(1, 2, 2)
plt.plot(samples, tempList, color="#264653")
plt.title("Samples over temperature")
plt.xlabel("Samples")
plt.ylabel("Temperature")

plt.show()