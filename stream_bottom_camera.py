"""
Author: Jacob Pitsenberger
Program: stream_bottom_camera.py
Version: 1.0
Project: TelloEDU Demos
Date: 6/28/2023
Purpose: This module demonstrates using openCV with the TelloEDU mini drone to stream video from its bottom camera.
"""
import sys
import cv2
from djitellopy import tello


def run_bottom_video(drone):
    """ The downward camera is a grey-only 320x240 IR-sensitive camera so need to resize to only get the part of the
    returned frames with visible image (noise in bottom of frame otherwise). To switch view to bottom camera calling
    set_video_direction() on the TEllO object with drone.CAMERA_DOWNWARD as its directional parameter before calling
    streamon() in the main method. For more info on this see the djitellopy tello.py module code."""
    while True:
        # Get the most recent frame
        frame = drone.get_frame_read().frame
        # Crop the frame to only show non-noise part (the visible image)
        crop_img = frame[0:240, 0:320]
        # Show the cropped image
        cv2.imshow("Frame", crop_img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # Cleanup and end the program.
            cv2.destroyAllWindows()
            print("Ending the Tello Object...")
            drone.end()
            sys.exit("Tello Object Deleted. Exiting the code with sys.exit()!")


def main():
    # Connect to the drone, set its video direction, and start receiving video
    drone = tello.Tello()
    drone.connect()
    drone.set_video_direction(drone.CAMERA_DOWNWARD)
    drone.streamon()
    run_bottom_video(drone)


if __name__ == "__main__":
    main()
