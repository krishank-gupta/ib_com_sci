# Import libraries
import requests
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
from library import get_data

temp_15 = get_data(15)
print(temp_15)
temp_17 = get_data(17)
print(temp_17)
temp_19 = get_data(19)
print(temp_19)
hum_16 = get_data(16)
print(hum_16)
hum_18 = get_data(18)
print(hum_18)
hum_20 = get_data(20)
print(hum_20)

raw_temp_mean = []
raw_temp_mean_samples = []
raw_hum_mean = []
raw_hum_mean_samples = []

for i in range(0, len(temp_15), 1):
    data = [temp_15[i],temp_17[i], temp_19[i]]
    raw_temp_mean.append(np.mean(data))

for i in range(0, len(hum_20), 1):
    data = [hum_16[i], hum_18[i], hum_20[i]]
    raw_hum_mean.append(np.mean(data))

for i in range(0,len(raw_temp_mean),1):
    raw_temp_mean_samples.append(i)

for i in range(0,len(raw_hum_mean),1):
    raw_hum_mean_samples.append(i)

# smoothing
samplesPerHour = 4 # 1 sample per 5mins
temp_15_mean_hour = []
temp_17_mean_hour = []
temp_19_mean_hour = []
temp_21_mean_hour = []
hum_16_mean_hour = []
hum_18_mean_hour = []
hum_20_mean_hour = []

temp_samples = []
hum_samples = []

for t in range(0, len(temp_15), samplesPerHour):
    temp_15_mean_hour_var = temp_15[t:t+samplesPerHour]
    temp_17_mean_hour_var = temp_17[t:t+samplesPerHour]
    temp_19_mean_hour_var = temp_19[t:t+samplesPerHour]
    # temp_21_mean_hour_var = temp_21[t:t+samplesPerHour]

    # hum_mean_hour_var = temp[t:t+samplesPerHour]
    temp_15_mean_hour.append(sum(temp_15_mean_hour_var) / len(temp_15_mean_hour_var))
    temp_17_mean_hour.append(sum(temp_17_mean_hour_var) / len(temp_17_mean_hour_var))
    temp_19_mean_hour.append(sum(temp_19_mean_hour_var) / len(temp_19_mean_hour_var))
    # temp_21_mean_hour.append(sum(temp_21_mean_hour_var) / len(temp_21_mean_hour_var))

for t in range(0, len(hum_20), samplesPerHour):
    hum_16_mean_hour_var = hum_16[t:t+samplesPerHour]
    hum_18_mean_hour_var = hum_18[t:t+samplesPerHour]
    hum_20_mean_hour_var = hum_20[t:t+samplesPerHour]

    hum_16_mean_hour.append(sum(hum_16_mean_hour_var) / len(hum_16_mean_hour_var))
    hum_18_mean_hour.append(sum(hum_18_mean_hour_var) / len(hum_18_mean_hour_var))
    hum_20_mean_hour.append(sum(hum_20_mean_hour_var) / len(hum_20_mean_hour_var))

for t in range(0, len(temp_15_mean_hour), 1):
    temp_samples.append(t)

for t in range(0, len(hum_16_mean_hour), 1):
    hum_samples.append(t)

# Calc Mean
temp_mean = []
hum_mean = []
temp_mean_samples = []
hum_mean_samples = []

for i in range(0, len(temp_15_mean_hour),1):
    data = [temp_15_mean_hour[i],temp_17_mean_hour[i], temp_19_mean_hour[i]]

    temp_mean.append(np.mean(data))
    temp_mean_samples.append(i)

for i in range(0, len(hum_16_mean_hour), 1):
    data = [hum_16_mean_hour[i], hum_18_mean_hour[i], hum_20_mean_hour[i]]

    hum_mean.append(np.mean(data))
    hum_mean_samples.append(i)


# Model
t1,t2,t3,t4 = np.polyfit(temp_mean_samples, temp_mean, 3)
h1,h2,h3,h4 = np.polyfit(hum_mean_samples, hum_mean, 3)

non_linear_model_temp_x = []
non_linear_model_hum_x = []
non_linear_model_temp_y = []
non_linear_model_hum_y = []

for i in (temp_mean_samples):
    non_linear_model_temp_y.append(t1*(i**3) + t2*(i**2) + t3*i + t4)

for i in (hum_mean_samples):
    non_linear_model_hum_y.append(h1*(i**3) + h2*(i**2) + h3*i + h4)

for idx in range(0, len(temp_mean), 1):
    non_linear_model_temp_x.append(idx)

for idx in range(0, len(hum_mean), 1):
    non_linear_model_hum_x.append(idx)


# Prediction
temp_predictions = []
hum_predictions = []
prediction_samples = []

for i in range(len(temp_mean_samples), len(temp_mean_samples) + 24, 5):
    temp_predictions.append(t1*(i**3) + t2*(i**2) + t3*i + t4)
    hum_predictions.append(h1*(i**3) + h2*(i**2) + h3*i + h4)
    prediction_samples.append(i)

print(f"Temperature model formula: {t1:.5f}x^3 + {t2:.5f}x^2 + {t3:.5f}x + {t4:.5f}")
print(f"Humidity model formula: {h1:.5f}x^3 + {h2:.5f}x^2 + {h3:5f}x + {h4:.5f}")

plt.style.use('ggplot')
plt.figure(figsize=(16,8))

# Graph Remote Data and Smoothing (93-125)
# Raw temperature
plt.subplot(4,1,1)
plt.plot(raw_temp_mean_samples, raw_temp_mean)
# plt.title("Samples over temperature") 
plt.xlabel("Samples")
plt.ylabel("Temperature")

# Smoothed Temperature
plt.subplot(4, 1, 2)
plt.plot(temp_mean_samples, temp_mean, color="#264653")
plt.plot(non_linear_model_temp_x, non_linear_model_temp_y)
# plt.errorbar(temp_mean_samples, temp_mean, standard_deviation, fmt = "o", color = "#e76f51")

plt.plot(prediction_samples, temp_predictions, "b+")

# plt.title("Samples over Temperature per hour")
plt.xlabel("Samples")
plt.ylabel("Hourly Temperature")
plt.axhline(y=max(temp_mean), color="#ff000033")
plt.axhline(y=min(temp_mean), color="#00ff1e33")
plt.axhline(y=np.mean(temp_mean), color="#ffd50033")

# # Raw Humidity
plt.subplot(4,1,3)
plt.plot(raw_hum_mean_samples, raw_hum_mean)
# plt.title("Samples over Humidity") 
plt.xlabel("Samples")
plt.ylabel("Humidity")

# # Smoothed Humidity
plt.subplot(4, 1, 4)
plt.plot(hum_mean_samples, hum_mean, color="#264653")
plt.plot(non_linear_model_hum_x, non_linear_model_hum_y)
plt.plot(prediction_samples, hum_predictions, 'b+')
# plt.title("Samples over Humidity per hour")
plt.xlabel("Samples")
plt.ylabel("Hourly Humidity")
plt.axhline(y=max(hum_mean), color="#ff000033")
plt.axhline(y=min(hum_mean), color="#00ff1e33")
plt.axhline(y=np.mean(hum_mean), color="#ffd50033")

plt.show()



# # Grid
# fig=plt.figure(figsize=(14,10))
# grid = gridspec.GridSpec(3,3,figure=fig)

# box1=fig.add_subplot(grid[0:3,0:2])
# plt.plot(hum_mean_samples, hum_mean, 'red')
# plt.title('Average')

# datas = [hum_16_mean_hour, hum_18_mean_hour, hum_20_mean_hour]
# for i in range(0, 3, 1):
#     box=fig.add_subplot(grid[i,2])
#     plt.plot(samples, datas[i])
#     plt.title(f"Sensor {i+1}")

# fig=plt.figure(figsize=(14,10))
# grid = gridspec.GridSpec(3,3,figure=fig)

# box1=fig.add_subplot(grid[0:3,0:2])
# plt.plot(temp_mean_samples, temp_mean, 'red')
# plt.title('Average')

# datas = [temp_15_mean_hour, temp_17_mean_hour, temp_19_mean_hour]
# for i in range(0, 3, 1):
#     box=fig.add_subplot(grid[i,2])
#     plt.plot(samples, datas[i])
#     plt.title(f"Sensor {i+1}")

# plt.show()
