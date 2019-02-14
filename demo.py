#!/usr/bin/env python3
# -*- coding: utf-8 -*
from composant import*
from fenetre import*
from terrain import*
#from ObjetPhysique import*
#from Vecteur import*
#from Robot import*
#import math

"""Le but ici, est de constuire quelques objets simples, un robot et de les afficher"""


"""Test rendu graphique arène :"""

arene = Terrain()
arene.objet.append(ObjetPhysique(50, 40, 0, 40, 10))
arene.objet.append(ObjetPhysique(400, 360, 0, 50, 30))
arene.objet.append(ObjetPhysique(780, 250, 0, 30, 30))
robot = Robot(500, 200, 0)
arene.robot.append(robot)
fenetre = Fenetre(arene)

"""
arene = Terrain()
fenetre = Fenetre(arene)
"""
