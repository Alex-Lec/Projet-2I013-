#!/usr/bin/env python3
# -*- coding: utf-8 -*


class Robot():#(ObjetPhysique):
    """
    Classe Robot :
    position (x, y);
    Camera;
    Roue droite, gauche;
    Detecteur;
    Acceleremetre.
    """

    def __init__(self, x, y, z, dir, camera, rd, rg, detecteur, accelerometre):
       # ObjetPhysique(x, y, z, dir)
        self.x=x
        self.y=y
        self.z=z
        self.camera = camera
        self.rd = rd
        self.rg = rg
        self.detecteur = detecteur
        self.accelerometre = accelerometre
        
    def printPos(self):
        print("position : x= ", self.x ," et y = ", self.y)

    def avancer(self, x, y):
        self.printPos()
        print("avancer de x= ", x, " et de y = ", y)
        self.x+=x
        self.y+=y
        self.printPos()
        

    def reculer(self, x, y):
        self.x=self.x-x
        self.y=self.y-y
        

    def tourner(self, angle):
        pass
    
    