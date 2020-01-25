import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 120)
# cap.set(3, 1920)
# cap.set(4, 1080)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
# cap = cv2.VideoCapture("WIN_20200112_15_04_22_Pro.mp4")

print(cap.get(cv2.CAP_PROP_CONTRAST))
print(cap.get(cv2.CAP_PROP_EXPOSURE))
# cap.set(cv2.CAP_PROP_CONTRAST, 32)  # 32
# cap.set(cv2.CAP_PROP_EXPOSURE, -0.25)  # -6
# print(cap.get(cv2.CAP_PROP_CONTRAST))
# print(cap.get(cv2.CAP_PROP_EXPOSURE))
# print(cap.get(cv2.CAP_PROP_FPS))
# fourcc = cv2.VideoWriter_fourcc(*"XVID")
# out = cv2.VideoWriter("test.avi", fourcc, 20.0, (640, 480))

clip_width = 40
while True:
    _, frame = cap.read()
    frame_time = time.perf_counter()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, gray_binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)    #127
    if clip_width == 0:
        gray_binary_clipped = gray_binary
    else:
        gray_binary_clipped = gray_binary[:, clip_width:-clip_width]
    # print(gray_binary.shape[1])
    # print(gray_binary_clipped.shape[1])
    # breakpoint()

    # out.write(frame)
    # print(np.count_nonzero(gray_binary[:, 0]), np.count_nonzero(gray_binary[:, -1]),
    #       np.count_nonzero(gray_binary[0, :]), np.count_nonzero(gray_binary[-1, :]), time.perf_counter())
    # print(time.perf_counter(), np.count_nonzero(gray_binary[:, 0]) - np.count_nonzero(gray_binary[:, -1]))
    h = gray_binary_clipped.shape[1]//2
    left_area = np.count_nonzero(gray_binary_clipped[:, :h])
    right_area = np.count_nonzero(gray_binary_clipped[:, h:])
    area_difference = right_area - left_area
    area_sum = right_area + left_area
    angle = np.arctan(area_difference/(h**2))
    print(frame_time, area_difference, area_sum)

    cv2.imshow("gray", gray)
    cv2.imshow("gray_binary_clipped", gray_binary_clipped)
    # cv2.imshow("gray_binary_flip", gray_binary_flip)
    # cv2.imshow("gray_binary_xor", gray_binary_xor)

    # with open("9_35_pm_1_15_2020.tsv", "a+") as write_line:
    #     write_line.write(str(frame_time) + "\t" + str(area_difference) + "\t" + str(area_sum) + "\n")

    # Wait for escape key
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
# out.release()
cv2.destroyAllWindows()
