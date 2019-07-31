import numpy as np

# Import data
data_array = np.loadtxt("CoolTerm Capture 2019-07-29 11-46-17.txt")

# Convert times from interval to cumulative
times_cumulative = np.zeros_like(data_array[:, 0])
times_cumulative[0] = data_array[0, 0]
for i in range(len(times_cumulative)-1):
    times_cumulative[i + 1] = data_array[i + 1, 0] + times_cumulative[i]
print(data_array[:, 0])
print(times_cumulative)
