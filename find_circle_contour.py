# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 11:58:15 2018

@author: Umanga Poudel
"""

"""
To see if a circle a circle is enclosed or not.
We will take a video or live feed, get the circles using hough circles,
crop out the circle and sorrounding 10 pixels,
then use flood fill algorithm to check if there is a leak.
Can use histograms or contours to differentiate between the two.
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0) #replace 0 with path to read in a video.

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (720, 560))
    frame_2 = frame.copy()
    frame_2 = cv2.cvtColor(frame_2, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    mask_2 = np.zeros(frame.shape[:2], dtype = 'uint8')
    
    circles = cv2.HoughCircles(frame_gray, cv2.HOUGH_GRADIENT, 1, 50)
#    print(circles)
    if circles is not None:
        try:
            circles = np.round(circles[0, :]).astype("int")
    
            for (x, y, r) in circles:
    #            cv2.circle(frame, (x,y), r, (0, 255, 0), 4)
                cv2.rectangle(frame, (x-2, y-2), (x + 2, y + 2), (0, 0, 255), -1)
                cv2.rectangle(mask_2, (x-r-10, y-r-10), (x + r + 10, y + r + 10), (255, 255, 255), -1)
        
            masked = cv2.bitwise_and(frame_2, frame_2, mask = mask_2)
            masked = masked[y-r-10:y+r+10, x-r-10:x+r+10]
            cv2.imshow("Masked", masked)
            
            ret, otsu = cv2.threshold(masked.copy(), 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
#            ret_t, otsu = cv2.threshold(masked.copy(),127,255,cv2.THRESH_BINARY_INV)
            
            h, w = otsu.shape[:2]
            mask = np.zeros((h+2, w+2), np.uint8)
            # Floodfill from point (h/2, w/2)
            cv2.floodFill(otsu, mask, (int(h/2), int(w/2)), 255)
            
            cv2.imshow("Flood_fill", otsu)
            cnts = cv2.findContours(otsu, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
            cnts = cnts[1]
            for c in cnts:
                ((x, y), radius) = cv2.minEnclosingCircle(c)
                    #Plot the circle.
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 0), 2)
        except: pass
    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(50) & 0xFF
    if key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()


            




