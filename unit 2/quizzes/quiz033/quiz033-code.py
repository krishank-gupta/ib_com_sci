import matplotlib.pyplot as plt
import requests

plt.style.use('ggplot')

url = "http://192.168.6.142/"


def get_sensor_data(sensor_id:int)->list:
    
    response = requests.get(url + 'readings')
    data = response.json()
    data = data['readings'][0]
    
    output = []
    
    for i in data:
        if i['sensor_id'] == sensor_id:
            output.append(i['value'])
    return output

data_needed_sensors = [6,8,9,10]
for sensor in data_needed_sensors:
    data_of_sensor = get_sensor_data(sensor)

    print(data_of_sensor)