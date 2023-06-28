"""
Author: Jacob Pitsenberger
Program: recognize_face.py
Version: 1.0
Project: TelloEDU Demos
Date: 6/27/2023
Purpose: This module demonstrates using openCV with the TelloEDU mini drone or a computers web camera
         to perform real-time facial recognition.

---ADAPTED FROM---
Title: FACE RECOGNITION + ATTENDANCE PROJECT | OpenCV Python | Computer Vision
Author: Murtaza's Workshop - Robotics and AI
Date: 6-11-20
Code Version: N/A
Availability: https://www.youtube.com/watch?v=sz25xxF_AVE&t=957s
"""
import sys

import cv2
from djitellopy import tello
import face_recognition
import numpy as np
import os

path = 'data-files\\faces'
images = []

# Take names from images and put them in a list
classNames = []
myList = os.listdir(path)
# print(myList)
for cl in myList:
    curframe = cv2.imread(f'{path}/{cl}')
    images.append(curframe)
    classNames.append(os.path.splitext(cl)[0])

def findEncodings(images):
    encodeList = []
    for frame in images:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(frame)[0]
        encodeList.append(encode)
    return encodeList


encodeListKnown = findEncodings(images)
print('Encoding Complete')

def faceRec(frame):
    # reduce size of image to speed up process since doing in real time
    # Scale factor of .15 requires closer distance to face to recognize

    # frameS = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
    frameS = cv2.resize(frame, (0, 0), None, 0.15, 0.15)

    # Convert to RGB color space for use with face_recognition library
    frameS = cv2.cvtColor(frameS, cv2.COLOR_BGR2RGB)

    # Find the location of faces then send to encoding fxn
    facesCurFrame = face_recognition.face_locations(frameS)
    encodesCurFrame = face_recognition.face_encodings(frameS, facesCurFrame)

    # Find the matches by iterating through faces in current frame and comparing them with all encodings found b4
    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # Lowest Distance will be our best match
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            y1, x2, y2, x1 = faceLoc

            # Multiply by 4 to maintain OG value if using scale factor of .25 to resize
            # Multiply by 7 for .15 scale factor resize

            # y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            y1, x2, y2, x1 = y1 * 7, x2 * 7, y2 * 7, x1 * 7

            cv2.rectangle(frame, (x1, y1-50), (x2, y2+10), (0, 255, 0), 2)
            cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, .65, (255, 255, 255), 2)

def run_computer_video(cap):
    """For use in main with openCV capture object"""
    while True:
        ret, frame = cap.read()
        faceRec(frame)
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


def run_tello_video(drone):
    """For use in main with djitellopy tello object"""
    while True:
        frame = drone.get_frame_read().frame
        faceRec(frame)
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            print("Ending the Tello Object...")
            drone.end()
            sys.exit("Tello Object Deleted. Exiting the code with sys.exit()!")

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
