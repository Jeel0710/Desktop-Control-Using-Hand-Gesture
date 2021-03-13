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

while True:
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)
    mx, my, cat = hdet(frame, min_YCrCb, max_YCrCb)

    if mx==0 and my==0:
        sys.exit()

    if cat=='2':
        cv2.putText(frame,"Two", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
        pai.click(mx, my)
    elif cat=='0':
        cv2.putText(frame,"Zero", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
        pai.dragTo(mx, my)
    else:
        cv2.putText(frame,"One or any other", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
        pai.moveTo(mx, my)
        
    
    cv2.imshow('frame', frame)
    


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

