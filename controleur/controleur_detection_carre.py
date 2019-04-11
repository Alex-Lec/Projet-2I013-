#!/usr/bin/env python3
# -- coding: utf-8 -

from strategie import StratAvance, StratStop, StratTourne, StratGetImage
from threading import Thread
from composant import vecteur
import time
import math
import numpy as np
import cv2 as cv
import sys

class Controleur_detection_carre():
    def __init__(self, rob, dst = 100, vit = 500):
        self.robot = rob
        self.Go = None
        self.cnt = 2
        self.dst = dst
        self.vitesse = vit

    def start(self):
        self.Go = StratAvance(self.robot, 100, self.vitesse)
        self.Go.start()
        self.cnt = 2

    def step(self):

        self.Go.step()
        
        if (self.robot.get_distance() <= self.dst):
            if (self.cnt != 0):
                self.Go = StratStop(self.robot)
                self.Go.start()
                self.cnt = 0
        
        elif (self.robot.get_distance() <= (2*self.dst)):
            if (self.cnt == 0):
                self.Go = StratAvance(self.robot, 100, self.vitesse/2)
                self.Go.start()
                self.cnt = 2
        
            elif (self.cnt != 1):
                self.Go.update(self.vitesse/2)
                self.cnt = 1
        
        elif (self.cnt != 2 ):
            self.Go = StratAvance(self.robot, 100, self.vitesse)
            self.Go.start()
            self.cnt = 2

        if (self.cnt == 0):

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

                cv.drawContours(image,[cnt],-1,(0,255,0),2)

                if len(approx)==4 and perimetre > 20:
                    (x, y, w, h) = cv.boundingRect(approx)
                    ratio = w / float(h)
                    if ratio >= 0.95 and ratio <= 1.05:
                        shape = "carre"
                    else:
                        shape = "rectangle"

                    cv.putText(image, shape, (cX, cY), cv.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)

                    if (shape == 'carre' or shape == 'rectangle'):
                        print(cX, cY)

                        if (cX >= 500):
                            print(cX - 500)
                        else:
                            print(500 - cX)

                """
                if len(approx)==3:
                    shape = "triangle"
                elif len(approx)==4:
                    (x, y, w, h) = cv.boundingRect(approx)
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
                """

                """
                cv.imshow('image.jpeg', image)
                cv.waitKey(0)
                cv.destroyAllWindows()
                """

            cv.imwrite('image.jpeg', image)

    def stop(self):
        if (self.cnt == 0):
            return False
        return True