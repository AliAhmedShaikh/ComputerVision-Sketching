# -*- coding: utf-8 -*-
"""
Created on Tue May 19 22:15:13 2020

@author: Ali Ahmed Shaikh
"""

import cv2  
#path = 'C:\\Users\\DELL\\Pictures\\Camera Roll\\WIN_20241215_20_47_34_Pro.jpg'
color_image = cv2.imread("image.png")  
#color_image = cv2.imread(path)
cv2.imshow("image",color_image)  

cartoon_image1, cartoon_image2  = cv2.pencilSketch(color_image, sigma_s=60, sigma_r=0.5, shade_factor=0.02)

cv2.imshow('pencil sketch', cartoon_image1)  
cv2.waitKey()  
cv2.destroyAllWindows()   