#!/usr/bin/env python3
# -*- coding: utf-8 -*

import numpy as np
import math

class Vecteur():
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vector = np.array([self.x, self.y, self.z])  
	
    def produitScalaire(self, s):
        self.x *= s
        self.y *= s
        self.z *= s

    def produitScalaire_vectors(self, v):
        return self.x * v.x + self.y + v.y + self.z * v.z

    def norme_vecteur(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2))
	
    def produitVectoriel(self, v):
        return np.cross(self, v)

    def cosinus_2_vectors(self, v):
        return (self.produitScalaire_vectors(v)) / (self.norme_vecteur() * v.norme_vecteur())

    def arcos(self, v, deg = 'True'):
        if (deg == 'True'):
            return math.acos((self.produitScalaire_vectors(v)) / (self.norme_vecteur() * v.norme_vecteur()))
        else:
            return math.acos((self.produitScalaire_vectors(v)) / (self.norme_vecteur() * v.norme_vecteur())) 

    def add(self, v):
        return Vecteur(self.x + v.x, self.y + v.y, self.z + v.z)
        
    def sub(self, v):
        return Vecteur(self.x - v.x, self.y - v.y, self.z - v.z)