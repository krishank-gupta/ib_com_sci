import matplotlib.pyplot as plt

plt.style.use('ggplot')

data = [57.0, 56.0, 57.0, 56.0, 55.0, 55.0, 54.0, 54.0, 54.0, 53.0, 53.0, 54.0, 53.0, 53.0, 52.0, 52.0, 51.0, 51.0, 51.0, 50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 48.0, 49.0, 49.0, 48.0, 48.0, 48.0, 49.0]

samples = []
samplesPerHour = 4

for i in range(0, len(data), 1):
    samples.append(i)


# Original Data graph
plt.subplot(3,1,1)
plt.plot(samples, data, 'o-', color="#264653")

# Smoothed version
smooth_size = 4
data_smooth = []
smooth_x = []

for i in range(0, len(data), smooth_size):
    values = data[i:(i+smooth_size)]
    data_smooth.append( sum(values) / smooth_size )
    smooth_x.append(i)

plt.subplot(3,1,2)
plt.plot(smooth_x, data_smooth, 'o-', color='#364653')

# HL Smoothing Window 50%
smooth_size_50 = 4
data_smooth_50 = []
smooth_x_50 = []

for i in range(0, len(data), (smooth_size_50//2)):
    values = data[i:(i+smooth_size_50)]
    data_smooth_50.append( sum(values) / smooth_size_50 )
    smooth_x_50.append(i)

plt.subplot(3,1,3)
plt.plot(smooth_x_50[0:-1], data_smooth_50[0:-1], 'o-', color='#364653')

plt.show()

