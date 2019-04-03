#!/usr/bin/env python3
# -*- coding: utf-8 -*
#import pyglet
import time
#from OpenGL.GL import glLight
#from pyglet.gl import *
#from pyglet.window import key
#from OpenGL.GLUT import *
#from pyglet.image.codecs.png import PNGImageDecoder

from .vecteur import Vecteur
import numpy as np
from math import radians,sqrt, cos, sin, pi
class ObjetPhysique:

    def __init__(self, x = 0, y = 0, z = 0, largeur = 50, longueur = 100, hauteur = 20, r = 50, g = 50, b = 0):
       
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
    
        points = [[self.x -self.longueur//2, self.y - self.largeur//2],\
            [self.x + self.longueur//2, self.y - self.largeur//2],\
            [self.x + self.longueur//2, self.y + self.largeur//2],\
            [self.x - self.longueur//2, self.y + self.largeur//2]]


        VecteurDirection = (self.v_dir.x,self.v_dir.y,self.v_dir.z)
        v_direction =    VecteurDirection / np.linalg.norm(VecteurDirection)

        
        VecteurDefaut = (1,0,0)
        v_defaut = VecteurDefaut/np.linalg.norm(VecteurDefaut)

        if (self.v_dir.y > 0):
            angle = np.arccos(np.clip(np.dot(v_direction, v_defaut), -1.0, 1.0))
        else :
            angle = 2*pi-np.arccos(np.clip(np.dot(v_direction, v_defaut), -1.0, 1.0))

        cos_val = cos(angle)
        sin_val = sin(angle)

        new_points = []
        for x_old, y_old in points:
            x_old -= self.x
            y_old -= self.y
            x_new = x_old * cos_val - y_old * sin_val
            y_new = x_old * sin_val + y_old * cos_val
            new_points.append([x_new + self.x, y_new + self.y])
        
        return new_points
        
        
    def draw(self):
        v_y = self.v_dir.y
        v_x = self.v_dir.x
        
        v_xg = -self.v_dir.y
        v_yg = self.v_dir.x
        
        v_xd = self.v_dir.y
        v_yd = -self.v_dir.x
        
        v_xb = -self.v_dir.x
        v_yb = -self.v_dir.y
        
        """
        glBegin(GL_QUADS)
        glColor3ub(self.r,self.g,self.b)
        
        glVertex3f(v_xb*self.longueur/2 + v_xg*self.largeur/2,
                   v_yb*self.longueur/2 + v_yg*self.largeur/2,
                   self.z)# point 1
    
        glVertex3f(v_xb*self.longueur/2 + v_xg*self.largeur/2,
                   v_yb*self.longueur/2 + v_yg*self.largeur/2,
                   self.z + self.hauteur)# point 2
    
        glVertex3f(v_x*self.longueur/2 + v_xg*self.largeur/2,
                   v_y*self.longueur/2 + v_yg*self.largeur/2,
                   self.z)# point 3
    
        glVertex3f(v_x*self.longueur/2 + v_xg*self.largeur/2,
                   v_y*self.longueur/2 + v_yg*self.largeur/2,
                   self.z+self.hauteur)# point 4
                   
        glVertex3f(v_x*self.longueur/2 + v_xd*self.largeur/2,
                   v_y*self.longueur/2 + v_yd*self.largeur/2,
                   self.z)# point 5
                   
        glVertex3f(v_x*self.longueur/2 + v_xd*self.largeur/2,
                   v_y*self.longueur/2 + v_yd*self.largeur/2,
                   self.z + self.hauteur)# point 6
                
        glVertex3f(v_xb*self.longueur/2 + v_xd*self.largeur/2,
                   v_yb*self.longueur/2 + v_yd*self.largeur/2,
                   self.z)# point 7
                   
        glVertex3f(v_xb*self.longueur/2 + v_xd*self.largeur/2,
                   v_yb*self.longueur/2 + v_yd*self.largeur/2,
                   self.z + self.hauteur)# point 8
                   
        glEnd()
        """
                
                
                
                
                
                   
                   
                   
