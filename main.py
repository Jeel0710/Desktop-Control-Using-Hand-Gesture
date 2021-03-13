import cv2
import numpy as np
import sys
import pyautogui as pai
from detect_hand import hdet


pai.FAILSAFE = False

scr_wid, scr_ht = pai.size()
print(scr_wid, scr_ht)

cap = cv2.VideoCapture(0)

min_YCrCb = np.array([0, 130, 70], np.uint8)
max_YCrCb = np.array([255, 180, 130], np.uint8)
