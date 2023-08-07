"""
Author: Jacob Pitsenberger
Program:stream_video.py
Version: 1.0
Project: TelloEDU Demos
Date: 8/7/2023
Purpose: This module demonstrates using openCV with the TelloEDU mini drone to stream video from its camera.
"""

import cv2
from djitellopy import tello


def run_tello_video(drone):
    """For use in main with djitellopy tello object"""
    while True:
        frame = drone.get_frame_read().frame
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()


def main():
    # Initialize Drone Object.
    drone = tello.Tello()
    # Establish connection with the drone.
    drone.connect()
    # Start the drones camera stream.
    drone.streamon()
    # Call the function to stream video from the drone.
    run_tello_video(drone)


if __name__ == "__main__":
    main()
