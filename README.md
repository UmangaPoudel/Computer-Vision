# Computer-Vision

In 2018, I was writing these computer vision scripts for edge computing on Raspberry Pi.

OpenCV, Python
 
hsv_value_select.py  
  Takes in a video file or a live feed.   
  Select at least 1 point; takes the last 10 points to give you the range of the pixels in the object.  
  Press "w" to start selecting points.  
  Press "r" to see the lower vrange and upper range.  
  Press "q" to quit.  

frame_select.py  
  Let's the user draw rectangles on the image and get the co-ordinates of the rectangle.  
  Useful if you want to make your own annotatin software, want to mask out your ergion.  
  etc.  
  
find_circle_contour.py  
  To see if a circle a circle is enclosed or not.  
  We will take a video or live feed, get the circles using hough circles,  
  crop out the circle and sorrounding 10 pixels,  
  then use flood fill algorithm to check if there is a leak.  
  Can use histograms or contours to differentiate between the two.  
