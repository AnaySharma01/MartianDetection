import cv2
import numpy as np

def MartianDetected(frame):
    # Applies gaussian blur, median blur, and canny edge detection on the image
    # https://github.com/adityagandhamal/road-lane-detection/blob/master/detection_on_vid.py Lines 35-38
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Defines variables
    detected = False
    point = ""
    # Read the alien template
    template = cv2.imread('img.png', 0)

    # Checks the resolution of each point
    resolution = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)

    # Specify a threshold
    threshold = 0.45

    # https://www.geeksforgeeks.org/template-matching-using-opencv-in-python/
    # Store the coordinates of matched area in a numpy array
    loc = np.where(resolution >= threshold)

    # Detects the Martian
    for point in zip(*loc[::-1]):
        if point in zip(*loc[::-1]):
            detected = True
            print("detected")


