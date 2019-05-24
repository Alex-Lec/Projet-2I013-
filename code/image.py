# !/usr/bin/env python3
# -- coding: utf-8 -

import pyglet
from pyglet.gl import *
from pyglet.window import key
from OpenGL.GLUT import *
from OpenGL.GL import glLight
from pyglet.image.codecs.png import PNGImageDecoder
from PIL import Image
from pyglet import image
import random
import numpy as np
import cv2

img = Image.open('image.jpeg')
rbg_img = img.convert('RGB')
rbg_img.save('image.jpeg')

"""
image = cv2.imread('screenshot.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,200,255,cv2.THRESH_BINARY_INV)
contours,h = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    perimetre=cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,0.01*perimetre,True)
    
    M = cv2.moments(cnt)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    cv2.drawContours(image,[cnt],-1,(0,255,0),2)
    if len(approx)==3:
        shape = "triangle"
    elif len(approx)==4:
        (x, y, w, h) = cv2.boundingRect(approx)
        ratio = w / float(h)
        if ratio >= 0.95 and ratio <= 1.05:
            shape = "carre"
        else:
            shape = "rectangle"
    elif len(approx)==5:
        shape = "pentagone"
    elif len(approx)==6:
        shape = "hexagone"
    else:
        shape= "circle"
    cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""