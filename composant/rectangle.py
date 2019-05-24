#!/usr/bin/env python3
# -*- coding: utf-8 -*

from .objetphysique import ObjetPhysique
import numpy as np
from math import radians,sqrt, cos, sin, pi
import pyglet
from pyglet.gl import *

class Rectangle(ObjetPhysique):

    def __init__(self, x = 0, y = 0, z = 0, largeur = 50, longueur = 100, hauteur = 20, r = 50, g = 50, b = 0):
        super().__init__(x, y, z, largeur, longueur, hauteur, r, g, b)

        x = self.x - (self.largeur / 2)
        y = self.y
        z = self.z - (self.longueur / 2)

        X = x + (self.largeur)
        Y = y + self.hauteur
        Z = z + (self.longueur)

        color = ('c3B', (r, g, b) * 4)

        self.batch = pyglet.graphics.Batch()

        self.batch.add(4, GL_QUADS, None, ('v3f', (x,y,z, x,y,Z, x,Y,Z, x,Y,z)), color)
        self.batch.add(4, GL_QUADS, None, ('v3f', (X,y,Z, X,y,z, X,Y,z, X,Y,Z)), color)
        self.batch.add(4, GL_QUADS, None, ('v3f', (x,y,z, X,y,z, X,y,Z, x,y,Z)), color)
        self.batch.add(4, GL_QUADS, None, ('v3f', (x,Y,Z, X,Y,Z, X,Y,z, x,Y,z)), color)
        self.batch.add(4, GL_QUADS, None, ('v3f', (X,y,z, x,y,z, x,Y,z, X,Y,z)), color)
        self.batch.add(4, GL_QUADS, None, ('v3f', (x,y,Z, X,y,Z, X,Y,Z, x,Y,Z)), color)

    def draw(self):
        self.batch.draw()
    
    def get_points(self):
    
        # Vecteur vers devant le robot
        v_x = self.v_dir.x*(self.longueur//2) 
        v_y = self.v_dir.y*(self.longueur//2)
        
        # Vecteur vers la gauche du robot
        v_xg = -self.v_dir.y*(self.largeur//2)
        v_yg =  self.v_dir.x*(self.largeur//2)
        
        # Vecteur vers la droite du robot
        v_xd =  self.v_dir.y*(self.largeur//2)
        v_yd = -self.v_dir.x*(self.largeur//2)
        
        # Vecteur vers derrière le robot
        v_xb = -self.v_dir.x*(self.longueur//2)
        v_yb = -self.v_dir.y*(self.longueur//2)
    
        # Premier point devant à gauche du robot, deuxiéme devant à droite du robot,...
        pts=[[self.x + v_x  + v_xg, self.y + v_y  + v_yg],\
             [self.x + v_x  + v_xd, self.y + v_y  + v_yd],\
             [self.x + v_xb + v_xd, self.y + v_yb + v_yd],\
             [self.x + v_xb + v_xg, self.y + v_yb + v_yg]]
        
        return pts


