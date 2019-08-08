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
window_start = 300
window_size = 2**6
data_array_sample = data_array[window_start:window_start+window_size, :]
# Remove offset
print(data_array_sample[:, 1].mean())
data_array_sample[:, 1] = data_array_sample[:, 1] - data_array_sample[:, 1].mean()
N = np.int_(data_array_sample[:, 0].max() - data_array_sample[:, 0].min())
print(N)
s = 2**24
print(N / s)
print(144e6 /(N / s))
y, x = signal.resample(data_array_sample[:, 1], s, t=data_array_sample[:, 0])
print("Resample Done")

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
print(len(convolve))
plt.plot(convolve)
plt.show()

# convolve2 = np.convolve(convolve, convolve, "full")
# plt.plot(convolve2)
# plt.show()
#
# convolve3 = np.convolve(convolve2, convolve2, "full")
# plt.plot(convolve3)
# plt.show()
#
# convolve4 = np.convolve(convolve3, convolve3, "full")
# plt.plot(convolve4)
# plt.show()

