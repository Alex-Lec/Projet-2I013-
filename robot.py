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

        self.vecteur_direction = Vecteur(1., 0., 0.)
        self.scalaire_rotation = 1
        self.scalaire_vitesse = 1
        
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

    def avancer(self):
        #self.printPos()
        #print("Avancer de x =", x, " et de y =", y)
        vx = self.vecteur_direction.x * self.scalaire_vitesse
        vy = self.vecteur_direction.y * self.scalaire_vitesse
        
        self.x += vx
        self.y += vy
        #self.printPos()

        #déplacer le centre
        self.center = (self.x,self.y)

        #déplacer les points
        new_points = []
        
        for x_old, y_old in self.points:
            new_points.append([x_old + vx, y_old + vy])
        self.points = new_points


    def tourner(self):
        #self.printPosCoin()
        angle = math.radians(1)
        cos_val = math.cos(angle)
        sin_val = math.sin(angle)
        cx, cy = self.x,self.y
        #self.center
        new_points = []
        
        x1 = self.vecteur_direction.x
        y1 = self.vecteur_direction.y
        
        self.vecteur_direction.x = x1*cos_val - y1*sin_val # On utilise round pour enlever
        self.vecteur_direction.y = x1*sin_val + y1*cos_val # les décimales inutiles
        
        for x_old, y_old in self.points:
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
