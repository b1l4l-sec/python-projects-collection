import cv2
import numpy as np

cap = cv2.VideoCapture(0)
back = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read() #hello in this video we ll turm my camera into just to display two colors white and black and this project just to detect the movement of the objects when ever it detects a movmt it displays its movmt lets see how it works
    fback = back.apply(frame)

    # cv2.imshow('main cam',frame)
    cv2.imshow('bBack',fback)

    key = cv2.waitKey(30) & 0xff
    if key == 27 :
        break
cap.release()
cv2.destroyAllWindows()