#!/usr/bin/env python3
# -*- coding: utf-8 -*

from .vecteur import Vecteur
import numpy as np
from math import radians,sqrt, cos, sin, pi
class Zones_Grises():

    def __init__(self, x = 0, y = 0, z = 0, largeur = 50, longueur = 100, hauteur = 20):
       
        self.x = x
        self.y = y
        self.z = z
        self.longueur = longueur
        self.largeur = largeur
        self.hauteur = hauteur
        self.v_dir = Vecteur(1., 0., 0.)
        self.vector = Vecteur(self.x, self.y, self.z)
        self.color = 'grey'

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
                   
    def check_robot_zone(self, robot):
        if ((robot.x - robot.longueur//2, robot.y - robot.largeur//2 >= self.x -self.longueur//2, self.y - self.largeur//2 and \
            robot.x + robot.longueur//2, robot.y - robot.largeur//2 <= self.x + self.longueur//2, self.y - self.largeur//2) or \
                (robot.x + robot.longueur//2, robot.y + robot.largeur//2 >= self.x + self.longueur//2, self.y + self.largeur//2 and \
                    robot.x - robot.longueur//2, robot.y + robot.largeur//2 <= self.x - self.longueur//2, self.y + self.largeur//2)):
            
            robot.vd /= 2
            robot.vg /= 2
            return True
        return False

