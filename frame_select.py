# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 10:51:23 2018

@author: Umanga Poudel
"""

"""
Let's the user draw rectangles on the image and get the co-ordinates of the rectangle.
Useful if you want to make your own annotatin software, want to mask out your ergion.
etc.
"""

import cv2

def _draw_roi(frame):
    fromCenter = False
    select_roi = cv2.selectROI("Frame", frame, fromCenter)
    return select_roi
    
def _get_first_frame():
    cap2 = cv2.VideoCapture(path)
    ret2, frame2 = cap2.read()
    frame2 = cv2.resize(frame2, (500, 400))
    return frame2
    key = cv2.waitKey(0) & 0xFF
    if key == ord("q"):
        cv2.destroyAllWindows()
    cap2.release()

def get_rois():
    print("Please select first region. Press Enter when selected.")
    first_roi = _draw_roi(_get_first_frame())
    print("First region selected is: {} {}".format(first_roi, '\n'))
    print("Please select second region. Press Enter when selected.")
    second_roi = _draw_roi(_get_first_frame())
    print("Second region selected is: {} {}".format(second_roi, '\n'))
    print("Please select third region. Press Enter when selected.")
    third_roi = _draw_roi(_get_first_frame())
    print("Third region selected is: {} {}".format(third_roi, '\n'))

path = r'C:/Users/poudelu/Desktop/Additional_files/test.mp4'

get_rois()
cap = cv2.VideoCapture(path) #replace path with 0 for live video.
while (cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (500, 400))
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
        
    if key == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()