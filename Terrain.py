#!/usr/bin/env python3
# -*- coding: utf-8 -*

from ObjetPhysique import *

class Terrain():

    def __init__(self, dimx = 1000, dimy = 600):
        
        self.dimx = dimx
        self.dimy = dimy
        self.objet = list()
        self.robot = list()

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
            
    def afficher_terrain(self):
        pass
    
    def testCollision(self, i1, i2):
        o1 = self.objet[i1]
        o2 = self.objet[i2]
        ovx = min(o1.get_x() + o1.get_cote(), o2.get_x() + o2.get_cote()) - max(o1.get_x() - o1.get_cote(), o2.get_x() - o2.get_cote()) > 0
        ovy = min(o1.get_y() + o1.get_cote(), o2.get_y() + o2.get_cote()) - max(o1.get_y() - o1.get_cote(), o2.get_y() - o2.get_cote()) > 0
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
                if o1.get_x() + o1.get_cote() < o2.get_x() - o2.get_cote():
                    o2.set_x(o2.get_x() + (o2.get_x() - o2.get_cote() - o1.get_x() - o1.get_cote()) + 1)
                else:
                    o2.set_x(o2.get_x() - (o1.get_x() + o1.get_cote() - o2.get_x() + o2.get_cote()) - 1)
                if o1.get_y() + o1.get_cote() < o2.get_y() - o2.get_cote():
                    o2.set_y(o2.get_y() + (o2.get_y() - o2.get_cote() - o1.get_y() - o1.get_cote()) + 1)
                o1.set_dir(Vecteur(0.0,0.0,0.0).sub(o1.get_dir()))  
                o2.set_dir(Vecteur(0.0,0.0,0.0).sub(o2.get_dir()))
            
