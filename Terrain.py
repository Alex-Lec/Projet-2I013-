#!/usr/bin/env python3
# -*- coding: utf-8 -*

from ObjetPhysique import *
from Vecteur import *
from Camera import *
from Roue import *
from Detecteur import *
from Accelerometre import *
from Robot import *

class Terrain():

    def __init__(self, dimx = 1000, dimy = 600):
        
        self.dimx = dimx
        self.dimy = dimy
        self.objet = []
        self.robot = []
        ajouter_objets([ObjetPhysique(-1, 0, 0, 1, 600, 1), ObjetPhysique(0, -1, 0, 1000, 1, 1), ObjetPhysique(1001, 0, 0, 1, 600, 1), ObjetPhysique(0, 601, 0, 1000, 1, 1)])
        #On ajoute des obstacles autour du terrain à sa création pour éviter que des objets n'en sortent.
        
    # Problème de coohérence, soit on rajoute soit on créait
    """ 
        def ajouter_robot(self, x, y, z):
            c = Camera()
            rg = Roue()
            rd = Roue()
            d = Detecteur()
            a = Accelerometre()
            vdir = Vecteur(20, 0.0, 0.0)
            r = Robot(x, y, dir,)
            self.objet.append(r)
    """

    def ajouter_objets(self, o): #prend une liste d'object en arguement
        for i in o:
            self.objet.append(i)
            
    def ajouter_robots(self,o):
        for i in o:
            self.robot.append(i)
            
    
    def testCollision(self, i1, i2):
        o1 = self.objet[i1]
        o2 = self.objet[i2]
        ovx = min(o1.get_x() + o1.get_dim()[0], o2.get_x() + o2.get_dim()[0]) - max(o1.get_x() - o1.get_dim()[0], o2.get_x() - o2.get_dim()[0]) > 0
        ovy = min(o1.get_y() + o1.get_dim()[1], o2.get_y() + o2.get_dim()[1]) - max(o1.get_y() - o1.get_dim()[1], o2.get_y() - o2.get_dim()[1]) > 0
        return ovx & ovy
    
    def checkCollisions (self):
        for i in range(len(self.objet)):
            try:
                for j in range(len(self.objet)):
                    if i == j:
                        continue
                    if testCollision(i, j):
                        raise ValueError()
                        
            except ValueError:
                o1 = self.objet[i]
                o2 = self.objet[j]
                if o1.get_x() + o1.get_dim()[0] < o2.get_x() - o2.get_dim()[0]:
                    o2.set_x(o2.get_x() + (o2.get_x() - o2.get_dim()[0] - o1.get_x() - o1.get_dim()[0]) + 1)
                else:
                    o2.set_x(o2.get_x() - (o1.get_x() + o1.get_dim()[0] - o2.get_x() + o2.get_dim()[0]) - 1)
                if o1.get_y() + o1.get_dim()[1] < o2.get_y() - o2.get_dim()[1]:
                    o2.set_y(o2.get_y() + (o2.get_y() - o2.get_dim()[1] - o1.get_y() - o1.get_dim()[1]) + 1)
                o1.set_dir(Vecteur(0.0,0.0,0.0).sub(o1.get_dir()))  
                o2.set_dir(Vecteur(0.0,0.0,0.0).sub(o2.get_dir()))
            
