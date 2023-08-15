# TelloEDU-Examples

This repo contains scripts for demonstrating various uses of the TelloEDU drone.

## Table of Contents

- [Stream Video](#stream-video)
- [Stream Bottom Camera](#stream-bottom-camera)
- [Flight Data and Status Display](#flight-data-and-status-display)
- [Keyboard Control with OpenCV](#keyboard-control-with-opencv)
- [Blur Faces](#blur-faces)
- [Face Detection and Count](#face-detection-and-count)
- [Real-Time Facial Recognition](#real-time-facial-recognition)

## Stream Video

This module demonstrates using OpenCV with the TelloEDU mini drone to stream video from its camera.

**Author:** Jacob Pitsenberger
**Version:** 1.0
**Date:** 8/7/2023

### Purpose

This module showcases how to utilize OpenCV to stream real-time video from the TelloEDU mini drone's camera. By connecting to the drone and starting its camera stream, you can view the live video feed directly in an OpenCV window.

### Instructions

To run the module, ensure you have the required dependencies installed:

```bash
pip install 'djitellopy' 'opencv-python'
```

Run the script `stream_video.py` to start streaming the drone's camera video in real-time. The video feed will be displayed in a window. Press the 'q' key to close the video window and end the stream.

Note: Adjust the necessary sections in the script to connect to the drone and start the video stream.

---
**[View the module code](stream_video.py)**


## Stream Bottom Camera

This module demonstrates using OpenCV with the TelloEDU mini drone to stream video from its bottom camera.

**Author:** Jacob Pitsenberger
**Version:** 1.0
**Date:** 6/28/2023

### Purpose

This module showcases how to utilize OpenCV to stream real-time video from the TelloEDU mini drone's bottom camera. By connecting to the drone, setting its video direction to the bottom camera, and starting its camera stream, you can view the live video feed from the bottom camera in an OpenCV window.

### Instructions

To run the module, ensure you have the required dependencies installed:

```bash
pip install 'djitellopy' 'opencv-python'
```

Run the script `stream_bottom_camera.py` to start streaming the drone's bottom camera video in real-time. The video feed will be displayed in a window. Press the 'q' key to close the video window and end the stream.

Note: Make sure to adjust the relevant sections in the script to connect to the drone, set its video direction, and start the video stream for the bottom camera.

---
**[View the module code](stream_bottom_camera.py)**

## Flight Data and Status Display

This module demonstrates using OpenCV with the TelloEDU mini drone to obtain hardware and flight data from the drone and display it on the video stream.

**Author:** Jacob Pitsenberger
**Version:** 1.0
**Date:** 6/30/2023

### Purpose

This module showcases how to interact with the TelloEDU mini drone's hardware and obtain various flight data, such as orientation, battery level, height, distance to obstacle, temperature, and barometric pressure. The collected data is displayed on the video stream window in real-time, providing insights into the drone's status during flight.

### Instructions

To run the module, ensure you have the required dependencies installed:

```bash
pip install 'djitellopy' 'opencv-python'
```
Run the script `flight_data.py` to start streaming video from the TelloEDU drone's camera while simultaneously displaying flight data on the video stream. The data includes orientation angles, battery level, height, distance to obstacle, temperatures, and barometric pressure. Press the 'q' key to close the video window and end the stream.

Note: Make sure to adjust the relevant sections in the script to connect to the drone and start the video stream.

---
**[View the module code](flight_data.py)**

## Keyboard Control with OpenCV

This module demonstrates using OpenCV with the TelloEDU mini drone to stream video from the camera, control its movements, and take pictures using keyboard commands. The script allows you to interactively control the drone using the keyboard. You can take off, land, move in various directions, rotate, and capture images.

**Author:** Jacob Pitsenberger
**Version:** 1.0
**Date:** 8/14/2023

### Instructions

To run the module, ensure you have the required dependencies installed:


```bash
pip install 'djitellopy' 'opencv-python'
```

Run the script `keyboard_control_opencv.py` and follow the on-screen instructions to interact with the drone.

### Keyboard Controls

- **b**: Takeoff
- **e**: Land
- **p**: Take picture
- **q**: End program
- **w**: Go up
- **s**: Go down
- **i**: Go forward
- **k**: Go backward
- **j**: Go left
- **l**: Go right
- **a**: Rotate counter-clockwise
- **d**: Rotate clockwise

**Note:** There might be a delay in updating video frames when commands are being sent to the drone. Once the drone sends a response to a given movement or rotation command, the frames continue to update.

Feel free to modify the default speed and rotation values in the script according to your requirements.

---

**[View the module code](keyboard_control_opencv.py)**

## Blur Faces

This module demonstrates using OpenCV with the TelloEDU mini drone or a computer's web camera to detect faces in the camera stream and blur the surrounding areas.

**Author:** Jacob Pitsenberger
**Version:** 1.0
**Date:** 7/7/2023

### Purpose

This module showcases how to utilize OpenCV to detect faces in real-time camera streams and apply a blurring effect to the surrounding areas of the detected faces. Whether using the TelloEDU mini drone's camera or a computer's webcam, the module provides an interactive way to explore face detection and manipulation.

### Instructions

To run the module, ensure you have the required dependencies installed:

```bash
pip install opencv-python
```

Run the script `blur_faces.py` and follow the on-screen instructions to experience the face detection and blurring effects in real-time.

**Note:** If using the TelloEDU mini drone, make sure to adjust the relevant sections in the script to connect to the drone and start the video stream.

---
**[View the module code](blur_faces.py)**


## Face Detection and Count

This module demonstrates using OpenCV with the TelloEDU mini drone or a computer's web camera to perform facial detection and keep track of the number of faces detected at a given time.

**Author:** Jacob Pitsenberger
**Version:** 1.0
**Date:** 6/26/2023

### Purpose

This module showcases how to utilize OpenCV for real-time facial detection using the TelloEDU mini drone's camera or a computer's webcam. It detects faces in the camera stream and draws rectangles around them, along with counting the number of faces detected.

### Instructions

To run the module, ensure you have the required dependencies installed:

```bash
pip install opencv-python
```
Run the script `face_detect_and_count.py` and observe the facial detection in the video stream. The module will display the count of detected faces in the output.

Note: If using the TelloEDU mini drone, make sure to adjust the relevant sections in the script to connect to the drone and start the video stream.

---
**[View the module code](face_detect_and_count.py)**

## Real-Time Facial Recognition

This module demonstrates using OpenCV with the TelloEDU mini drone or a computer's web camera to perform real-time facial recognition.

**Author:** Jacob Pitsenberger
**Version:** 1.0
**Date:** 6/27/2023

### Purpose

This module showcases how to utilize OpenCV and the face_recognition library to perform real-time facial recognition using the TelloEDU mini drone's camera or a computer's webcam. It detects faces in the camera stream, compares them with known faces, and labels them with their recognized names.

### Attribution

This module has been adapted from the following source:
Title: FACE RECOGNITION + ATTENDANCE PROJECT | OpenCV Python | Computer Vision
Author: Murtaza's Workshop - Robotics and AI
Date: 6-11-20
Availability: [YouTube Video](https://www.youtube.com/watch?v=sz25xxF_AVE&t=957s)

### Instructions

To run the module, ensure you have the required dependencies installed:

```bash
pip install opencv-python face-recognition djitellopy
```

Download and save the images of the known faces in the 'data-files/faces' directory.

Run the script `recognize_face.py` and observe the real-time facial recognition and labeling in the video stream.

Note: If using the TelloEDU mini drone, make sure to adjust the relevant sections in the script to connect to the drone and start the video stream.

---
**[View the module code](recognize_face.py)**




