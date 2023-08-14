# TelloEDU-Examples

This repo contains scripts for demonstrating various uses of the TelloEDU drone.

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