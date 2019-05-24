#!/usr/bin/env python3
# -*- coding: utf-8 -*

from .objetphysique import ObjetPhysique
import numpy as np
from math import radians,sqrt, cos, sin, pi
import pyglet
from pyglet.gl import *

class Sol(ObjetPhysique):
    def __init__(self, x = 750, y = 450, z = 0, largeur = 5000, longueur = 5000, hauteur = 1, \
        r = 255, g = 255, b = 255):

        super().__init__(x, y, z, largeur, longueur, hauteur, r, g, b)

        color = ('c3B', (r, g, b) * 4)
        color_lines = ('c3B', (0, 0, 0) * 2)

        self.batch = pyglet.graphics.Batch()

        hauteur = 150

        self.batch.add(4, GL_QUADS, None, ('v3f', (0,0,0, 0,0,900, 1500,0,900, 1500,0,0)), color)

        """
        self.batch.add(2, GL_LINES, None, ('v3f', (0,hauteur,0, 1500,hauteur,900)), color_lines)
        self.batch.add(2, GL_LINES, None, ('v3f', (0,hauteur,900, 1500,hauteur,0)), color_lines)
        self.batch.add(2, GL_LINES, None, ('v3f', (0,hauteur,0, 1500,hauteur,0)), color_lines)
        self.batch.add(2, GL_LINES, None, ('v3f', (0,hauteur,0, 0,hauteur,900)), color_lines)
        self.batch.add(2, GL_LINES, None, ('v3f', (1500,hauteur,0, 1500,hauteur,900)), color_lines)
        self.batch.add(2, GL_LINES, None, ('v3f', (0,hauteur,900, 1500,hauteur,900)), color_lines)
        """
   
    def draw(self):
        self.batch.draw()