#Imports necessary packages
import cv2 as cv

def displayImage(image):
    #Returns the processed image
    cv.imshow("VideoWithLines", image)
    cv.waitKey(1)
