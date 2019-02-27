#!/usr/bin/env python3
# -*- coding: utf-8 -*
from composant import*
from principal import*

"""Le but ici, est de constuire quelques objets simples, un robot et de les afficher"""


"""Test rendu graphique arène :"""

arene = Terrain()
arene.objet.append(ObjetPhysique(50, 40, 0, 40, 10))
arene.objet.append(ObjetPhysique(100, 100, 0, 10, 100, 10))
arene.objet.append(ObjetPhysique(780, 250, 0, 30, 30))
robot = Robot(500, 200, 0,arene)
arene.robot.append(robot)
fenetre = Fenetre(arene)

"""
arene = Terrain()
fenetre = Fenetre(arene)
"""
