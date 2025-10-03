import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 280) # in this video i made a code in python to detect just the color that i have chose like red blue ... and not to display other colors it will display just the color that i want to see
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 220)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red color
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)

    # Blue color
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    # Green color
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)

    # # purple color
    # low_purple = np.array([75, 0, 130])
    # high_purple = np.array([192, 128, 255])
    # purple_mask = cv2.inRange(hsv_frame, low_green, high_green)
    # purple = cv2.bitwise_and(frame, frame, mask=green_mask)

    # Every color except white
    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])
    mask = cv2.inRange(hsv_frame, low, high)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    
    
    cv2.imshow("Frame", frame)
    cv2.imshow("Red", red)
    cv2.imshow("Blue", blue)
    cv2.imshow("Green", green)
    # cv2.imshow("Purple", purple)
    cv2.imshow("NO white", result) # that s all for now u can practice and and any colors u want to detect seee uuuuuuuuuuuuuu

    key = cv2.waitKey(1)
    if key == 27:
        break