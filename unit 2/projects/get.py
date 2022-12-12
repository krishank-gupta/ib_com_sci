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
    # if data[i]['sensor_id'] in range(15,23,1):
        # print(data[i])

    if data[i]['sensor_id'] == 4:
        campus_hum.append(data[i]['value'])
    elif data[i]['sensor_id'] == 5:
        campus_temp.append(data[i]['value'])
    
start = 0
end = 576
campus_temp = campus_temp[start:end]
campus_hum = campus_hum[start:end]
raw_samples = []
for i in range(0,len(campus_hum),1):
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
    samples.append(t)

print(temp_mean_hour, len(temp_mean_hour))
print(hum_mean_hour, len(hum_mean_hour))


# Non-linear Modeling
a1_temp, a2_temp, a3_temp = np.polyfit(samples, temp_mean_hour, 2)
a1_hum, a2_hum, a3_hum = np.polyfit(samples, temp_mean_hour, 2)

non_linear_model_temp_x = []
non_linear_model_temp_y = []
non_linear_model_hum_x = []
non_linear_model_hum_y = []

for idx,i in enumerate(raw_samples):
    non_linear_model_temp_y.append(a1_temp*(i**2) + a2_temp*i + a3_temp)
    non_linear_model_temp_x.append(idx)
    non_linear_model_hum_y.append(a1_hum * (i**2) + a2_hum*i + a3_hum)
    non_linear_model_hum_x.append(idx)

# Prediction for 12 hours

temp_predictions = []
hum_predictions = []
prediction_samples = []

for i in range(end, end+144, 5):
    temp_predictions.append(a1_temp*(i**2) + a2_temp*i + a3_temp)
    hum_predictions.append(a1_hum*(i**2) + a2_hum*i + a3_hum)
    prediction_samples.append(i)


plt.style.use('ggplot')
plt.figure(figsize=(16,8))

# Raw temperature
plt.subplot(4,1,1)
plt.plot(raw_samples, campus_temp)
# plt.title("Samples over temperature") 
plt.xlabel("Samples")
plt.ylabel("Temperature")

# Smoothed Temperature
plt.subplot(4, 1, 2)
plt.plot(samples, temp_mean_hour, color="#264653")
plt.plot(non_linear_model_temp_x, non_linear_model_temp_y)
plt.plot(prediction_samples, temp_predictions, "b+")

# plt.title("Samples over Temperature per hour")
plt.xlabel("Samples")
plt.ylabel("Hourly Temperature")

# # Raw Humidity
plt.subplot(4,1,3)
plt.plot(raw_samples, campus_hum)
# plt.title("Samples over Humidity") 
plt.xlabel("Samples")
plt.ylabel("Humidity")

# # Smoothed Humidity
plt.subplot(4, 1, 4)
plt.plot(samples, hum_mean_hour, color="#264653")
plt.plot(non_linear_model_hum_x, non_linear_model_hum_y)
plt.plot(prediction_samples, hum_predictions, 'b+')
# plt.title("Samples over Humidity per hour")
plt.xlabel("Samples")
plt.ylabel("Hourly Humidity")

plt.show()

