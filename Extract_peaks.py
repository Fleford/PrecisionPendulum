import numpy as np

# log = np.loadtxt("9_35_pm_1_15_2020.tsv")
# x = log[:, 1]
# # x = np.array([0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1])
#
# # print(len(x))
#
# # Makes a list of indexes with positive peaks on them
# peak_time_list = []
# for i in range(1, len(x) - 1):
#     # Check if its a positive point
#     if x[i] >= x[i-1] and x[i] > x[i+1]:
#         # print("peak found at index " + str(i))
#         peak_time_list.append(log[i, 0])
# # print("peak_list: " + str(peak_list))
# np.savetxt("peak_time_list.txt", peak_time_list)

peak_time_list = np.loadtxt("peak_time_list.txt")
print(len(peak_time_list))


# Reports the difference between adjacent elements
offset = 1
# for offset in range(1, len(peak_time_list) - 100, 100):
while offset < len(peak_time_list) - 100:
    offset = 100
    difference_list = []
    # offset = 60
    for i in range(offset, len(peak_time_list)):
        # # Find anomalies
        if peak_time_list[i] - peak_time_list[i-offset] > 5.1:
            print(i, peak_time_list[i], peak_time_list[i-offset], peak_time_list[i] - peak_time_list[i-offset])
        difference_list.append(peak_time_list[i] - peak_time_list[i-offset])
    breakpoint()
    # print("difference_list: " + str(difference_list))
    # print("std: ", np.std(difference_list))
    # print("mean", np.mean(difference_list))
    # print("std/mean", np.std(difference_list)/np.mean(difference_list))
    print(offset, np.std(difference_list)/np.mean(difference_list), len(difference_list))
    breakpoint()
    # np.savetxt("peak_time_diff_8000_list.txt", difference_list)