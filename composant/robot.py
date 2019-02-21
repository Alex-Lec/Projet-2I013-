#!/usr/bin/env python3
# -*- coding: utf-8 -*

from .objetphysique import ObjetPhysique
from .vecteur import Vecteur
from .detecteur import Detecteur

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
        self.scalaire_rotation = 0
        self.scalaire_vitesse = 0
        self.detecteur = Detecteur
        """self.camera = camera
        self.rd = rd
        self.rg = rg
        self.detecteur = detecteur
        self.accelerometre = accelerometre"""

    def detecte(self,obj):
        print(self.detecteur.detecter(self,self,obj))
        
    def update(self):
        vx = self.vecteur_direction.x * self.scalaire_vitesse
        vy = self.vecteur_direction.y * self.scalaire_vitesse
        
        self.x += vx
        self.y += vy
        
        angle = math.radians(self.scalaire_rotation)
        cos_val = math.cos(angle)
        sin_val = math.sin(angle)
        
        x1 = self.vecteur_direction.x
        y1 = self.vecteur_direction.y
        
        self.vecteur_direction.x = x1*cos_val - y1*sin_val
        self.vecteur_direction.y = x1*sin_val + y1*cos_val
        
        for i in range(len(self.points)):
            j = self.points[i]
            
            self.points[i]= (j[0] + vx, j[1] + vy)
            
            x_new = (j[0] - self.x) * cos_val - (j[1] - self.y) * sin_val
            y_new = (j[0] - self.x) * sin_val + (j[1] - self.y) * cos_val
            
            self.points[i]= (x_new + self.x, y_new + self.y)
        
