import time
from .vecteur import Vecteur
import numpy as np
from math import radians,sqrt, cos, sin, pi
class ObjetPhysique:
    def __init__(self, x = 0, y = 0, z = 0,\
     largeur = 50, longueur = 100, hauteur = 20, r = 50, g = 50, b = 0):
       
        self.x = x
        self.y = y
        self.z = z
        
        self.longueur = longueur
        self.largeur = largeur
        self.hauteur = hauteur
        
        self.v_dir = Vecteur(1., 0., 0.)
        
        self.r = r
        self.g = g
        self.b = b
        
        
    def get_points(self):
        pass
