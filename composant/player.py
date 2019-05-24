#!/usr/bin/env python3
# -*- coding: utf-8 -*

from .objetphysique import ObjetPhysique
import numpy as np
from math import radians,sqrt, cos, sin, pi
import pyglet
from pyglet.gl import *
from pyglet.window import key
import math

class Player():

    """
    Cette classe correspond à la caméra
    Elle est définie par sa position et son orientation
    """

    def __init__(self,pos=(0,0,0),rot=(0,0), largeur = 1, longueur = 1, hauteur = 1):

        self.pos = list(pos)
        self.rot = list(rot)
        self.largueur = largeur
        self.longueur = hauteur
        self.hauteur = longueur
        
    def mouse_motion(self,dx,dy):
        dx /= 8; dy /= 8; self.rot[0] += dy; self.rot[1] -= dx
        if self.rot[0] > 90: self.rot[0] = 90
        elif self.rot[0]<-90: self.rot[0] = -90

    def update(self,dt,keys):
        s = dt*20
        rotY = -self.rot[1]/180*math.pi
        dx,dz = s*math.sin(rotY),s*math.cos(rotY)

        if (keys[key.Z]):
            self.pos[0]+=dx*10
            self.pos[2]-=dz*10

        if (keys[key.S]):
            self.pos[0]-=dx*10
            self.pos[2]+=dz*10

        if (keys[key.Q]):
            self.pos[0]-=dz*10
            self.pos[2]-=dx*10

        if (keys[key.D]):
            self.pos[0]+=dz*10
            self.pos[2]+=dx*10

        if (keys[key.SPACE]):
            self.pos[1]+=s

        if (keys[key.LSHIFT]):
            self.pos[1]-=s