#!/usr/bin/env python3
# -*- coding: utf-8 -*
from test import*
from Fenetre import*
from Terrain import*
from ObjetPhysique import*
from Vecteur import*
from Robot import*

"""Le but ici, est de constuire quelques objets simples, un robot et de les afficher"""

"""
v1 = Vecteur(200, 60, 30)
v2 = Vecteur(70, 350, 30)
v3 = Vecteur(100, 100, 30)
vrob = Vecteur(50,100,10)

ob1 = ObjetPhysique(20, 60, 0, 200, 60, 30)
ob2 = ObjetPhysique(900, 200, 0, 70, 350, 30)
ob3 = ObjetPhysique(600, 100, 0, 100, 100, 30)
ob4 = ObjetPhysique(230,500,0, 100, 100, 30)
robot = Robot(0, 300, 0)

arene = Terrain()
arene.ajouter_objets([ob1,ob2,ob3,ob4])
arene.ajouter_robots([robot])
fenetre = Fenetre(arene)
fenetre.affichage_arene()
arene.ajouter_objets([ObjetPhysique(200,300,0,50,70,70)])
fenetre.affichage_arene()
"""
"""
for i in range(100):
    robot.avancer(0,1)
    print
    fenetre.affichage_arene()


#fenetre.mainloop()
"""


"""Test rendu graphique arène :"""

arene = Terrain()
arene.objet.append(ObjetPhysique(50, 40, 0, 40, 10))
arene.objet.append(ObjetPhysique(400, 360, 0, 50, 30))
arene.objet.append(ObjetPhysique(780, 250, 0, 30, 30))
arene.robot.append(Robot(500, 200, 0))
fenetre = Fenetre(arene)
