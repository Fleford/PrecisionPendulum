import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
# Number of sample points
N = 100000
# sample spacing
T = 1.0 / 1000.0
x = np.linspace(0.0, N*T, N)

print(len(x))       # N = number of samples
print((x.max() - x.min())/len(x))        # T = time interval

y = np.sin(100.0 * 2.0*np.pi*x) + 0.6*np.sin(200.0 * 2.0*np.pi*x) + 2
yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), num=N//2)    # Array of the frequencies
# (0, 500)

plt.plot(xf[0:(N//2)//1], 2.0/N * np.abs(yf[0:(N//2)//1]))
plt.grid()
plt.show()
