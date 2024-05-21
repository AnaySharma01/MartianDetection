# Imports necessary packages
import cv2 as cv

# Imports functions for processing and displaying the frames
import ImageProcessing
import ImageDisplaying


def DisplayMartian():
    # https://geeksforgeeks.org/python-play-a-video-using-opencv/ lines 15 - 20
    # Variable needed for displaying the video
    videoIsPlaying = True

    # Starts the video capture
    video = cv.VideoCapture(0)

    # While the video is playing, read the frame, process it & display it
    while videoIsPlaying == True:
        videoIsPlaying, frame = video.read()
        ImageProcessing.MartianDetected(frame)
        ImageDisplaying.displayImage(frame)
    # Destroys the program when exiting
    cv.destroyAllWindows()


# Runs the program
DisplayMartian()

