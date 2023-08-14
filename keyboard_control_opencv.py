"""
Author: Jacob Pitsenberger
Program: keyboard_control_opencv.py
Version: 1.0
Project: TelloEDU Demos
Date: 8/14/2023
Purpose: This module demonstrates using openCV with the TelloEDU mini drone to stream video from camera and control
         its movements and take pictures using keyboard controls. Note that there is a delay in the updating of
         video frames when commands are being sent to the drone. Once the drone sends a response to a given movement
         or rotation command, the frames continue to update.
Use: Below are the keyboard controls for controlling the drones. To adjust the default speed or rotation values
     adjust the global constants that store these before launching the program.

-------------------------------CONTROLS-------------------------------

b - takeoff            a - rotate counter clock-wise            i - go forward
e - land               w - go up                                k - go backward
p - take picture       s - go down                              j - go left
q - end program        d - rotate clock-wise                    l - go right
----------------------------------------------------------------------
"""

import cv2
from djitellopy import tello
import os
import time
import numpy as np

# Define the height and width to resize the current frame to
FRAME_HEIGHT = 480
FRAME_WIDTH = 720
# Define the default DISTANCE value to move and the default DEGREE value to rotate.
MOVEMENT_DISTANCE = 20
ROTATION_DEGREE = 45

def take_picture(frame: np.ndarray) -> None:
    """Get the current frame then check if the pictures directory exists and if not create it.
    After this use imwrite to save the current frame to the images directory with the file name being
    the time the picture was taken.

    Args:
        frame (str): The current frame from the drone's camera stream.
    """
    if not os.path.exists("data-files/pictures"):
        os.mkdir("data-files/pictures")
    file_name = f"data-files/pictures/{time.time()}.png"
    cv2.imwrite(file_name, frame)
    print("Image saved:", file_name)
    time.sleep(0.3)

def control_drone(drone: tello.Tello) -> None:
    """Control the drone using keyboard commands and display camera feed.

    Args:
        drone (tello.Tello): The Tello drone object.
    """
    while True:
        # get the most recent frame from the drone, resize it, and display it on the screen.
        frame = drone.get_frame_read().frame
        frame = cv2.resize(frame, (FRAME_WIDTH, FRAME_HEIGHT))
        cv2.imshow("Frame", frame)
        # Set up the waitKey for updating the video stream
        key = cv2.waitKey(1) & 0xFF
        # Check for keyboard interactions and perform respective functionalities.
        if key == ord('q'):
            break
        elif key == ord('b'):
            print("Taking off. Please wait...")
            drone.takeoff()
            print("Done moving. Waiting for next command...")
        elif key == ord('e'):
            print("Landing. Please wait...")
            drone.land()
            print("Done moving. Waiting for next command...")
        elif key == ord('p'):
            print("Taking picture...")
            take_picture(frame)
        elif key in (ord('w'), ord('s'), ord('i'), ord('k'), ord('j'), ord('l')):
            # Dictionary to map keyboard commands to drone movement directions and distances.
            direction_mapping = {
                ord('w'): ("up", MOVEMENT_DISTANCE),
                ord('s'): ("down", MOVEMENT_DISTANCE),
                ord('i'): ("forward", MOVEMENT_DISTANCE),
                ord('k'): ("back", MOVEMENT_DISTANCE),
                ord('j'): ("left", MOVEMENT_DISTANCE),
                ord('l'): ("right", MOVEMENT_DISTANCE)
            }
            # Extract the drone movement command and distance from the dictionary based on the pressed key.
            key_command, value = direction_mapping[key]
            # Print a message indicating the movement command that will be executed.
            print(f"Moving {key_command.replace('_', ' ')}. Please wait...")
            # Call the corresponding drone movement method using getattr() and the extracted command and distance.
            getattr(drone, f"move_{key_command}")(value)
            # Print a message indicating that the movement is done and waiting for the next command.
            print("Done moving. Waiting for next command...")
        elif key in (ord('a'), ord('d')):
            # Dictionary to map keyboard commands to drone rotational directions and degrees.
            rotation_mapping = {
                ord('a'): "counter_clockwise",
                ord('d'): "clockwise"
            }
            # Extract the drone rotation command and degree from the dictionary based on the pressed key.
            key_command = rotation_mapping[key]
            # Print a message indicating the rotation command that will be executed.
            print(f"Rotating {key_command.replace('_', ' ')}. Please wait...")
            # Call the corresponding drone rotation method using getattr() and the extracted command and degree.
            getattr(drone, f"rotate_{key_command}")(ROTATION_DEGREE)
            # Print a message indicating that the rotation is done and waiting for the next command.
            print("Done rotating. Waiting for next command...")
    # If the 'q' key is pressed end the drone object and destroy all windows to end the program.
    drone.end()
    cv2.destroyAllWindows()


def main() -> None:
    """Main function to connect to the drone and control it."""
    # Initialize Drone Object.
    drone = tello.Tello()
    try:
        # Establish connection with the drone.
        drone.connect()
        # Start the drones camera stream.
        drone.streamon()
        # Call the drone controller function.
        control_drone(drone)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        # End the drone object and destroy all windows.
        drone.end()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
