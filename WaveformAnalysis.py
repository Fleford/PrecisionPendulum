import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# Import data
data_array = np.loadtxt("CoolTerm Capture 2019-07-29 11-46-17.txt")

# Convert times from interval to cumulative
times_cumulative = np.zeros_like(data_array[:, 0])
times_cumulative[0] = data_array[0, 0]
for i in range(len(times_cumulative)-1):
    times_cumulative[i + 1] = data_array[i + 1, 0] + times_cumulative[i]

# Replace interval times with cumulative times
data_array = np.insert(data_array, 1, times_cumulative, axis=1)   # Insert time_cumulative in the middle column
data_array = np.delete(data_array, 0, axis=1)   # Remove interval time column

# Pick out a sample of the data array
window_start = 3
window_size = 100
data_array_sample = data_array[window_start:window_start+window_size, :]
y, x = signal.resample(data_array_sample[:, 1], 2**24, t=data_array_sample[:, 0])

# print(x)
# print(y)

plt.plot(data_array_sample[:, 0], data_array_sample[:, 1])
plt.plot(x, y)
plt.show()
# print(data_array_sample)
