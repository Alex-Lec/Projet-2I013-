#!/usr/bin/env python3
# -- coding: utf-8 -

import time
import numpy as np
import cv2 as cv
import sys

class StratTraitementImage():
    def __init__(self, rob):
        self.robot = rob

    def start(self):
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
                self.cX = 0
                self.cY = 0
            else:
                self.cX = int(M["m10"] / M["m00"])
                self.cY = int(M["m01"] / M["m00"])

            cv.drawContours(image,[cnt],-1,(0,255,0),2)

            if len(approx)==4 and perimetre > 20:
                (x, y, w, h) = cv.boundingRect(approx)
                ratio = w / float(h)
                if ratio >= 0.95 and ratio <= 1.05:
                    shape = "carre"
                else:
                    shape = "rectangle"

                cv.putText(image, shape, (self.cX, self.cY), cv.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)

                if (shape == 'carre' or shape == 'rectangle'):
                    print(self.cX, self.cY)

                    if (self.cX >= 500):
                        print(self.cX - 500)
                        return self.cX - 500
                    else:
                        print(500 - self.cX)
                        return 500 - self.cX

    def step(self):
        pass

    def stop(self):
        return False
