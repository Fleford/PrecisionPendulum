import cv2
import numpy as np
import time

cap = cv2.VideoCapture(1)
# cap.set(3, 1920)
# cap.set(4, 1080)
# cap = cv2.VideoCapture("WIN_20200112_15_04_22_Pro.mp4")

# print(cap.get(cv2.CAP_PROP_CONTRAST))
# print(cap.get(cv2.CAP_PROP_EXPOSURE))
# cap.set(cv2.CAP_PROP_CONTRAST, 32)  # 32
# cap.set(cv2.CAP_PROP_EXPOSURE, -6)  # -6
# print(cap.get(cv2.CAP_PROP_CONTRAST))
# print(cap.get(cv2.CAP_PROP_EXPOSURE))
# print(cap.get(cv2.CAP_PROP_FPS))
# fourcc = cv2.VideoWriter_fourcc(*"XVID")
# out = cv2.VideoWriter("test.avi", fourcc, 20.0, (640, 480))

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_clip = gray[160:350, 100:400]
    _, gray_clip_binary = cv2.threshold(gray_clip, 100, 255, cv2.THRESH_BINARY) #127

    # out.write(frame)
    print(np.count_nonzero(gray_clip_binary), time.perf_counter())

    cv2.imshow("gray_clip_binary", gray_clip_binary)

    # Wait for escape key
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
# out.release()
cv2.destroyAllWindows()
