import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.fftpack import fft

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
print(len(data_array))
window_start = 1800
window_size = 2**6
data_array_sample = data_array[window_start:window_start+window_size, :]
# Remove offset
print(data_array_sample[:, 1].mean())
data_array_sample[:, 1] = data_array_sample[:, 1] - data_array_sample[:, 1].mean()
N = np.int_(data_array_sample[:, 0].max() - data_array_sample[:, 0].min())
print("N")
print(N)
x = np.linspace(data_array_sample[:, 0].min(), data_array_sample[:, 0].max(), num=2**24)
print("x.size")
print(x.size)
y = np.interp(x, data_array_sample[:, 0], data_array_sample[:, 1])
print("y.size")
print(y.size)

# s = 2**24
# print(N / s)
# print(144e6 /(N / s))
# y, x = signal.resample(data_array_sample[:, 1], s, t=data_array_sample[:, 0])
# print("Resample Done")

# N = len(x)     # Number of samples
# T = (x.max() - x.min()) / N   # Time interval between samples
# print(N, T)

# # Apply fft
# yf = fft(y)
# xf = np.linspace(0.0, 1.0/(2.0*T), N//2)    # Array of periods for the frequencies

# Show plot for input waveforms
plt.plot(data_array_sample[:, 0], data_array_sample[:, 1])
plt.plot(x, y)
plt.show()

# # Show plot for FFT
# plt.plot(xf[1:(N//2)//100000], 2.0/N * np.abs(yf[1:(N//2)//100000]))
# print(np.abs(yf[1:(N//2)//100000]).argmax())
# plt.grid()
# plt.show()

# correlate = np.correlate(y, y, "full")
# plt.plot(correlate)
# plt.show()


# convolve = np.convolve(y, y, "same")
# print(len(convolve))
convolve = signal.fftconvolve(y, y, mode='full')
convolve = signal.fftconvolve(convolve, convolve, mode='full')
print(len(convolve))
plt.plot(convolve)
plt.show()

# # Makes a list of indexes with positive peaks on them
# peak_list = []
# for i in range(1, len(convolve) - 1):
#     # Check if its a positive point
#     if convolve[i] > convolve[i-1] and convolve[i] > convolve[i+1]:
#         print("peak found at index " + str(i))
#         peak_list.append(i)
# print("peak_list: " + str(peak_list))
#
# # Reports the difference between adjacent elements
# difference_list = []
# for i in range(1, len(peak_list)):
#     difference_list.append(peak_list[i] - peak_list[i-1])
# print("difference_list: " + str(difference_list))

# difference_list - np.asarray(difference_list)
# print(np.median(np.asarray(difference_list)))
max = np.argmax(convolve)
min = np.argmin(convolve)
print(max - min)

