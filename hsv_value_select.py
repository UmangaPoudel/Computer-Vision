# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 4:13:34 2018

@author: Umanga Poudel
"""

"""
Takes in a video file or a live feed. 
Select at least 1 point; takes the last 10 points to give you the range of the pixels in the object.
Press "w" to start selecting points.
Press "r" to see the lower vrange and upper range.
Press "q" to quit.
"""

import cv2
import numpy as np
from collections import deque

path = r'C:/Users/poudelu/Desktop/Additional_files/test.mp4'


def click_for_coordinates(event, x,y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        coord_x = x
        coord_y = y
        bgr_values = frame[coord_y, coord_x]
        bgr_values = np.uint8([[[bgr_values[0], bgr_values[1], bgr_values[2]]]])
        hsv_values = cv2.cvtColor(bgr_values, cv2.COLOR_BGR2HSV)
        hue_deque.append(hsv_values[0][0][0])
        saturation_deque.append(hsv_values[0][0][1])
        value_deque.append(hsv_values[0][0][2])
#        print(hsv_values)
        
cap = cv2.VideoCapture(path) #replace path with 0 for live video.
hue_deque = deque(maxlen=10)
saturation_deque = deque(maxlen=10)
value_deque = deque(maxlen=10)

while (cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (500, 400))
    cv2.imshow("Frame", frame)
    
    lower_range = []
    upper_range = []
    
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord("q"):
        break
    
    if key == ord("w"):
        print("Please select 10 points. Select different points each time for the object. \nPress 'r' to see results.\nPress 'q' when done.")
        cv2.setMouseCallback("Frame", click_for_coordinates)
        
    if key == ord("r"):
        upper_range.append(max(list(hue_deque)))
        upper_range.append(max(list(saturation_deque)))
        upper_range.append(max(list(value_deque)))
        lower_range.append(min(list(hue_deque)))
        lower_range.append(min(list(saturation_deque)))
        lower_range.append(min(list(value_deque)))
        print("Lower_range is: ", lower_range)
        print("Upper range is: ", upper_range)
    
cap.release()
cv2.destroyAllWindows()





