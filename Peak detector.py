import numpy as np

x = np.array([0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1])

print(len(x))

# Makes a list of indexes with positive peaks on them
peak_list = []
for i in range(1, len(x) - 1):
    # Check if its a positive point
    if x[i] > x[i-1] and x[i] > x[i+1]:
        print("peak found at index " + str(i))
        peak_list.append(i)
print("peak_list: " + str(peak_list))

# Reports the difference between adjacent elements
difference_list = []
for i in range(1, len(x)):
    difference_list.append(x[i] - x[i-1])
print("difference_list: " + str(difference_list))
