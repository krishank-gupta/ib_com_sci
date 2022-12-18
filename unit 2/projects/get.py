# Import libraries
import requests
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

user = {
    "username": "Krish&Thumula",
    "password": "420deeznuts69"
}

# req = requests.post('http://192.168.6.142/login', json=user)
# access_token = req.json()["access_token"]

# auth = {"Authorization": f"Bearer {access_token}"}

# print(auth)

response = requests.get("http://192.168.6.142/readings")

data = response.json()
data = data['readings'][0]

campus_hum = []
campus_temp = []

for i in range(0, len(data), 1):
    # if data[i]['sensor_id'] == 15:
        # print(data[i]['datetime'], 15)
    if data[i]['sensor_id'] == 4:
        # print(data[i]['datetime'], 4)
        campus_hum.append(data[i]['value'])
    elif data[i]['sensor_id'] == 5:
        campus_temp.append(data[i]['value'])
        # print(data[i]['datetime'], 5)

start = 576*3
end = 576*4
prediction_hours = 12
prediction_mins = int(prediction_hours * 60 / 5)

campus_temp = campus_temp[start:end]
campus_hum = campus_hum[start:end]
raw_samples = []

for i in range(start,end,1):
    raw_samples.append(i)

# Smoothing
samplesPerHour = 12 # 1 sample per 5mins
temp_mean_hour = []
hum_mean_hour = []
samples = []

for t in range(0, len(campus_temp), samplesPerHour):
    temp_mean_hour_var = campus_temp[t:t+samplesPerHour]
    hum_mean_hour_var = campus_hum[t:t+samplesPerHour]
    temp_mean_hour.append(sum(temp_mean_hour_var) / len(temp_mean_hour_var))
    hum_mean_hour.append(sum(hum_mean_hour_var) / len(hum_mean_hour_var))

for t in range(start, end, samplesPerHour):
    samples.append(t)

print(temp_mean_hour, len(temp_mean_hour))
print(hum_mean_hour, len(hum_mean_hour))

# Non-linear Modeling
# a1_temp, a2_temp, a3_temp, a4_temp = np.polyfit(samples, temp_mean_hour, 3)
# a1_hum, a2_hum, a3_hum, a4_hum = np.polyfit(samples, temp_mean_hour, 3)
t1,t2,t3,t4 = np.polyfit(samples, temp_mean_hour, 3)
h1,h2,h3,h4 = np.polyfit(samples, hum_mean_hour, 3)

non_linear_model_x = []
non_linear_model_temp_y = []
non_linear_model_hum_y = []

for i in (raw_samples):
    non_linear_model_temp_y.append(t1*(i**3) + t2*(i**2) + t3*i + t4)
    non_linear_model_hum_y.append(h1*(i**3) + h2*(i**2) + h3*i + h4)


for idx in range(start, end, 1):
    non_linear_model_x.append(idx)


# Prediction for 12 hours
temp_predictions = []
hum_predictions = []
prediction_samples = []

for i in range(end, end+prediction_mins, 5):
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
plt.plot(raw_samples, campus_temp)
# plt.title("Samples over temperature") 
plt.xlabel("Samples")
plt.ylabel("Temperature")

# Smoothed Temperature
plt.subplot(4, 1, 2)
plt.plot(samples, temp_mean_hour, color="#264653")
plt.plot(non_linear_model_x, non_linear_model_temp_y)
plt.plot(prediction_samples, temp_predictions, "b+")

# plt.title("Samples over Temperature per hour")
plt.xlabel("Samples")
plt.ylabel("Hourly Temperature")
plt.axhline(y=max(temp_mean_hour), color="#ff000033")
plt.axhline(y=min(temp_mean_hour), color="#00ff1e33")
plt.axhline(y=np.mean(temp_mean_hour), color="#ffd50033")

# # Raw Humidity
plt.subplot(4,1,3)
plt.plot(raw_samples, campus_hum)
# plt.title("Samples over Humidity") 
plt.xlabel("Samples")
plt.ylabel("Humidity")

# # Smoothed Humidity
plt.subplot(4, 1, 4)
plt.plot(samples, hum_mean_hour, color="#264653")
plt.plot(non_linear_model_x, non_linear_model_hum_y)
plt.plot(prediction_samples, hum_predictions, 'b+')
# plt.title("Samples over Humidity per hour")
plt.xlabel("Samples")
plt.ylabel("Hourly Humidity")
plt.axhline(y=max(hum_mean_hour), color="#ff000033")
plt.axhline(y=min(hum_mean_hour), color="#00ff1e33")
plt.axhline(y=np.mean(hum_mean_hour), color="#ffd50033")

plt.show()