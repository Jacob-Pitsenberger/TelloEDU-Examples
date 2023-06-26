"""
Author: Jacob Pitsenberger
Program: face_detect_and_count.py
Version: 1.0
Project: TelloEDU Demos
Date: 6/26/2023
Purpose: This module demonstrates using openCV with the TelloEDU mini drone or a computers web camera
         to perform facial detection and keep a count of the number of faces detected at a given time.
"""

import cv2
from djitellopy import tello

def detect_faces(frame):
    """Print the number of faces detected in the drones camera stream to the output window and
    draws a box around any faces in the cv2 window if they are detected"""

    # Create a cascade
    faceCascade = cv2.CascadeClassifier("data-files\haarcascade_frontalface_default.xml")

    # Covert the frame to grayscale
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Get numpy array with values for faces detected by passing in grayscale image, scale factor, and minimum neighbors
    faces = faceCascade.detectMultiScale(frameGray, 1.2, 8)

    # For the x, y coordinates and width, height detected
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face using these values
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Update the face count with the number of faces detected
    face_count = "Faces: " + str(len(faces))

    # Print the face count as standard output
    print(face_count)

def run_computer_video(cap):
    """For use in main with openCV capture object"""
    while True:
        ret, frame = cap.read()
        detect_faces(frame)
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


def run_tello_video(drone):
    """For use in main with djitellopy tello object"""
    while True:
        frame = drone.get_frame_read().frame
        detect_faces(frame)
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
