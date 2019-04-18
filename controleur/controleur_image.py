#!/usr/bin/env python3
# -*- coding: utf-8 -*

from threading import Thread
from PIL import Image
import sys
import time
import numpy as np
#import cv2 as cv

class Controleur_image(Thread):
    def __init__(self, robot):
        Thread.__init__(self)
        self.robot = robot

    def start(self):

        time.sleep(0.5)
        self.robot.get_image()
        image = cv.imread('image.jpeg')
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        ret,thresh = cv.threshold(gray,180,255,cv.THRESH_BINARY_INV)
        contours,h = cv.findContours(thresh,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
        shape = None

        for cnt in contours:
            perimetre = cv.arcLength(cnt,True)
            approx = cv.approxPolyDP(cnt,0.01*perimetre,True)
            
            M = cv.moments(cnt)

            if (M["m00"] == 0):
                cX = 0
                cY = 0
            else:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])

            if (len(approx) == 4 or len(approx) == 5 or len(approx == 6)) and perimetre > 20:
                (x, y, w, h) = cv.boundingRect(approx)
                ratio = w / float(h)
                if (len(approx) == 5 or len(approx) == 6):
                    shape = "rectangle"
                elif ratio >= 0.95 and ratio <= 1.05:
                    shape = "carre"
                else:
                    shape = "rectangle"

                cv.drawContours(image,[cnt],-1,(0,255,0),2)
                cv.putText(image, shape, (cX, cY), cv.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
                cv.imwrite('image.jpeg', image)

                if (shape == 'carre' or shape == 'rectangle'):
                    print(cX, cY)

                    if (cX >= 500):
                        print(cX - 500)
                    else:
                        print(500 - cX)

    def step(self):
        pass

    def stop(self):
        False 
