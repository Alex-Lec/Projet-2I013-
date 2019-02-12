#!/usr/bin/env python3
# -*- coding: utf-8 -*

from Vecteur import *
from ObjetPhysique import*
import math
class Robot(ObjetPhysique):
    """
    Classe Robot :
    position (x, y);
    Camera;
    Roue droite, gauche;
    Detecteur;
    Acceleremetre.
    """

    def __init__(self, x, y, z): #dir, camera, rd, rg, detecteur, accelerometre):

        ObjetPhysique.__init__(self, x, y, z, largeur = 100, longueur = 50, hauteur = 25)
        self.points =   [ [x + 100//2 ,y  + 50//2 ],
                    [x + 100//2, y - 50 // 2],
                    [x - 100//2, y - 50//2],
                    [x - 100//2, y + 50//2]]
        self.center = (x,y)
        """self.camera = camera
        self.rd = rd
        self.rg = rg
        self.detecteur = detecteur
        self.accelerometre = accelerometre"""

    def printPos(self):
        print("position : x =", self.x ," et y =", self.y)
    def printPosCoin(self):
        i=1
        for point in self.points :
            x,y = point
            print ("position : x",i," = ", x ,"  y",i," = ",y)
            i+=1
    def avancer(self, x, y):
        self.printPos()
        print("Avancer de x =", x, " et de y =", y)
        self.x += x
        self.y += y
        self.center = (x,y)
        self.printPos()

    def reculer(self, x, y):
        self.printPos()
        print("Reculer de x =", x, " et de y =", y)
        self.x -= x
        self.y -= x
        self.printPos()

    def tourner(self, angle,points,center):
        #self.printPosCoin()
        angle = math.radians(angle)
        cos_val = math.cos(angle)
        sin_val = math.sin(angle)
        cx, cy = center
        new_points = []
        for x_old, y_old in points:
            x_old -= cx
            y_old -= cy
            x_new = x_old * cos_val - y_old * sin_val
            y_new = x_old * sin_val + y_old * cos_val
            new_points.append([x_new + cx, y_new + cy])
        self.points = new_points
        #self.printPosCoin()

"""
Test des méthodes avancer / reculer :
robot = Robot(10, 15, 0)
robot.avancer(10, 10)
robot.reculer(10, 10)
"""
