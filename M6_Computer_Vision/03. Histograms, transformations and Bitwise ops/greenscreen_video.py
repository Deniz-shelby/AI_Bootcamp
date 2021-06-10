import cv2
import numpy as np
import matplotlib.pyplot as plt

# CAPTURE VIDEO
video = cv2.VideoCapture(0)

while(video.isOpened()):
    check, frame = video.read()
    if frame is not None:
        # img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        img = frame
        hsv_m = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


        lower_yellow = (36, 25, 25)
        upper_yellow = (70, 255, 255)
        green_filter = cv2.inRange(hsv_m, lower_yellow, upper_yellow)
        masked_mm = img.copy()

        masked_mm[green_filter == 0] = [0, 0, 0]


        cv2.imshow('frame',masked_mm)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    else:
        break

#  rgba(170,177,38,255)
video.release()
cv2.destroyAllWindows()
cv2.waitKey(1)

