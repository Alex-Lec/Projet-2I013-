#!/usr/bin/env python3
# -*- coding: utf-8 -*
from Vecteur import*
from ObjetPhysique import*

class Robot(ObjetPhysique):
    """
    Classe Robot :
    position (x, y);
    Camera;
    Roue droite, gauche;
    Detecteur;
    Acceleremetre.
    """

    def __init__(self, x, y, z, vdim): #dir, camera, rd, rg, detecteur, accelerometre):
        ObjetPhysique.__init__(self, x, y, z, vdim)
        """self.camera = camera
        self.rd = rd
        self.rg = rg
        self.detecteur = detecteur
        self.accelerometre = accelerometre"""
        
    def printPos(self):
        print("position : x =", self.x ," et y =", self.y)

    def avancer(self, x, y):
        self.printPos()
        print("Avancer de x =", x, " et de y =", y)
        self.x += x
        self.y += y
        self.printPos()
        
    def reculer(self, x, y):
        self.printPos()
        print("Reculer de x =", x, " et de y =", y)
        self.x -= x
        self.y -= x
        self.printPos()
    
    def tourner(self, angle):
        pass

"""
Test des méthodes avancer / reculer :
robot = Robot(10, 15, 0)
robot.avancer(10, 10)
robot.reculer(10, 10)
"""
