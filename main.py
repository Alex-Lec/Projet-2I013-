#!/usr/bin/env python3
# -*- coding: utf-8 -*

import time
from diver import *
from controleur import Controleur_carre, Controleur_droit_stop, Controleur_image, Controleur_triangle, Controleur_polygone, Controleur_tour
import sys
from PIL import Image


robot_irl = True
dim = "0"
choix = "0"

try:
    from robot2I013.robot2I013 import Robot2I013
    robot = Robot2I013()
except(ImportError):
    from composant import *
    from code import *
    arene = Terrain()
    robot_irl = False
    print("\
    arene vide ->1\n\
    arene zone ->2")
    a = input()
    if (a == "2"):
        arene.zone.append(Zone(500, 25, 50, 50))
        arene.zone.append(Zone(1000, 25, 50, 50))
        arene.zone.append(Zone(500, 80, 50, 50))
        arene.zone.append(Zone(1000, 80, 50, 50))
        arene.zone.append(Zone(500, 135, 50, 50))
        arene.zone.append(Zone(1000, 135, 50, 50))
        arene.zone.append(Zone(725, 135, 50, 50))
        arene.zone.append(Zone(1225, 135, 50, 50))
        arene.zone.append(Zone(725, 190, 50, 50))
        arene.zone.append(Zone(1225, 190, 50, 50))
        arene.zone.append(Zone(725, 245, 50, 50))
        arene.zone.append(Zone(1225, 245, 50, 50))
        
        arene.zone.append(Zone(500, 245, 50, 50))
        arene.zone.append(Zone(1000, 245, 50, 50))
        arene.zone.append(Zone(500, 300, 50, 50))
        arene.zone.append(Zone(1000, 300, 50, 50))
        arene.zone.append(Zone(500,  355, 50, 50))
        arene.zone.append(Zone(1000, 355, 50, 50))
        arene.zone.append(Zone(725, 355, 50, 50))
        arene.zone.append(Zone(1225, 355, 50, 50))
        arene.zone.append(Zone(725, 410, 50, 50))
        arene.zone.append(Zone(1225, 410, 50, 50))
        arene.zone.append(Zone(725, 465, 50, 50))
        arene.zone.append(Zone(1225, 465, 50, 50))
        
    """
    arene.objet.append(ObjetPhysique(100, 20, 0, 50, 100, 100))
    arene.objet.append(ObjetPhysique(20, 100, 0, 100, 50, 100))
    arene.objet.append(ObjetPhysique(1300, 100, 50, 80, 70, 100))
    arene.objet.append(ObjetPhysique(500, 500, 10, 100, 100, 10))
    arene.objet.append(ObjetPhysique(780, 250, 0, 100, 50, 100))
    """
###################################################################

print("\n\n\
               Bienvenue dans la matrice\n\
               Selectionnez votre choix\n\n\
            #  Controleur_carre           -> 1 #\n\
            #  Controleur_droit_stop      -> 2 #\n\
            #  Controleur_triangle        -> 3 #\n\
            #  Controleur_polygone        -> 4 #\n\
            #  Controleur_tour_arene      -> 5 #\n\
            #  Controleur_image           -> 6 #\n\
            #  Quit                       -> Q #")

choix = input()


if not robot_irl :
    print("\n\
                   Controleur 2D ou 3D :            \n\n\
                #              2D   -> 1           #\n\
                #              3D   -> 2           #\n")
                
    dim = input()

if (dim == "1"):
    if (a == "2"):
        robot = Robot(x = 50, y = 50, z = 0, arene = arene)
    else :
        robot = Robot(x = 200, y = 200, z = 0, arene = arene)
    
elif (dim == "2"):
    robot = Robot(x = 200, y = 200, z = 0, \
    largeur = 10, longueur = 10, hauteur = 10, arene = arene)

if (choix == "1"):
    ctrc = Controleur_carre(robot,500,500)

elif (choix == "2"):
    ctrc = Controleur_droit_stop(robot, dst = 100)
    
elif (choix == "3"):
    ctrc = Controleur_triangle(robot)
    
elif (choix == "4"):
    print("\n\nNombre de cote :")
    cote = input()
    ctrc = Controleur_polygone(robot,int(cote))

elif (choix == "5"):
    ctrc = Controleur_tour(robot)

else :
    sys.exit()

###################################################################

if (not robot_irl and dim == "1"):
    arene.robot.append(robot)
    affichage = Affichage(arene)
    affichage.start()
    arene.start()

elif (not robot_irl and dim == "2"):
    arene.robot.append(robot)
    window = Window(arene = arene, width = 1000, height = 600, caption = 'Robot 2I013')
    window.start()
    arene.start()
    
tps = 100
ctrc.start()
while ctrc.stop():
    ctrc.step()
    print(robot.x, robot.y)
    time.sleep(1/tps)
    
print("stop")
sys.exit()
