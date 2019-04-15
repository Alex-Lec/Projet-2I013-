#!/usr/bin/env python3
# -*- coding: utf-8 -*

import time
from diver import *
from controleur import Controleur_carre, Controleur_droit_stop, Controleur_image
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
    arene.objet.append(ObjetPhysique(1300, 100, 100, 80, 70, 100))
    arene.objet.append(ObjetPhysique(500, 500, 10, 100, 100, 10))
    arene.objet.append(ObjetPhysique(780, 250, 0, 100, 50, 100))

###################################################################

print("\n\
               Bienvenue dans la matrice\n\
               Selectionnez votre choix\n\n\
            #  Controleur_carre           -> 1 #\n\
            #  Controleur_droit_stop      -> 2 #\n\
            #  Controleur_detection_carre -> 3 #\n\
            #  Controleur_balise          -> 4 #\n\
            #  Controleur_image           -> 5 #\n\
            #  Quit                       -> Q #")

choix = input()


if not robot_irl :
    print("\n\
                   Controleur 2D ou 3D :            \n\n\
                #              2D   -> 1           #\n\
                #              3D   -> 2           #\n")
                
    dim = input()

if (dim == "1"):
    robot = Robot(x = 100, y = 100, z = 0, arene = arene)
    
elif (dim == "2"):
    robot = Robot(x = 100, y = 100, z = 0, \
    largeur = 10, longueur = 10, hauteur = 10, arene = arene)

if (choix == "1"):
    ctrc = Controleur_carre(robot,500,500)

elif (choix == "2"):
    ctrc = Controleur_droit_stop(robot, dst = 100)
    
elif (choix == "5"):
    ctrc = Controleur_image(robot)

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
    time.sleep(1/tps)
    
print("stop")
sys.exit()
