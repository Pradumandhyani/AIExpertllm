import sys

print("Python:", sys.executable)

import mediapipe as mp
print("MediaPipe:", mp.__version__)

import cv2
print("OpenCV OK")

import numpy
print("NumPy OK")

from pycaw.pycaw import AudioUtilities
print("Pycaw OK")

import screen_brightness_control
print("Brightness OK")