"""
Author: Jacob Pitsenberger
Program: blur_faces.py
Version: 1.0
Project: TelloEDU Demos
Date: 7/7/2023
Purpose: This module demonstrates using openCV with the TelloEDU mini drone or a computers web camera
         to blur the area surrounding detected faces.
"""

import cv2
from djitellopy import tello

def blur_faces(frame):
    """Print the number of faces detected in the drones camera stream to the output window and
    draws a box around any faces in the cv2 window if they are detected"""

    # Create a cascade
    faceCascade = cv2.CascadeClassifier("data-files\haarcascade_frontalface_default.xml")

    # Covert the frame to grayscale
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Get numpy array with values for faces detected by passing in grayscale image, scale factor, and minimum neighbors
    face = faceCascade.detectMultiScale(frameGray, 1.2, 8)
    # For the x, y coordinates and width, height detected
    for (x, y, w, h) in face:
        # Instead of drawing a rectangle we will first calculate the end coordinates using its boxes start coordinates
        x2 = x + w
        y2 = y + h
        # Then we create a blured image for this area of the original frame
        blur_img = cv2.blur(frame[y:y2, x:x2], (50, 50))
        # And lastly we set detected area of the frame equal to the blurred image that we got from the area
        frame[y:y2, x:x2] = blur_img

def run_computer_video(cap):
    """For use in main with openCV capture object"""
    while True:
        ret, frame = cap.read()
        blur_faces(frame)
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


def run_tello_video(drone):
    """For use in main with djitellopy tello object"""
    while True:
        frame = drone.get_frame_read().frame
        blur_faces(frame)
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()


def main():
    # Connect to the drone and start receiving video
    # drone = tello.Tello()
    # drone.connect()
    # drone.streamon()
    # run_tello_video(drone)

    # Or create capture object for computers camera
    cap = cv2.VideoCapture(0)
    run_computer_video(cap)


if __name__ == "__main__":
    main()
