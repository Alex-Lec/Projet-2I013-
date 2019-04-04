#!/usr/bin/env python3
# -*- coding: utf-8 -*

import time
from diver import *
from controleur import Controleur_carre, Controleur_droit_stop, Controleur_image
import sys
from PIL import Image

robot_irl = True

try:
    from robot2I013.robot2I013 import Robot2I013
    robot = Robot2I013()
except(ModuleNotFoundError):
    from composant import *
    from code import *
    arene = Terrain()
    robot_irl = False

###################################################################
print("\n\
               Bienvenue dans la matrice\n\
               Selectionnez votre choix\n\n\
            #  Controleur_carre 2D      -> 1 #\n\
            #  Controleur_carre 3D      -> 2 #\n\
            #  Controleur_droit_stop 2D -> 3 #\n\
            #  Controleur_droit_stop 3D -> 4 #\n\
            #  get_image()              -> 5 #\n\
            #  Quit                     -> Q #")

choix = input()

if (choix == "1" or choix == "3"):
    robot = Robot(x = 100, y = 100, z = 0, arene = arene)
else:
    robot = Robot(x = 100, y = 100, z = 0, largeur = 100, longueur = 100, hauteur = 10, arene = arene)

if (choix == "1" or choix == "2"):
    ctrc = Controleur_carre(robot,500,500)
elif (choix == "3" or choix == "4"):
    ctrc = Controleur_droit_stop(robot)
elif (choix == "5"):
    ctrc = Controleur_image(robot)
else :
    sys.exit()

###################################################################

if (not robot_irl and (choix == "1" or choix == "3")):
    arene.robot.append(robot)
    affichage = Affichage(arene)
    affichage.start()
    arene.start()
    #img = Image.save(robot.get_image())

elif (not robot_irl and (choix == "2" or choix == "4")):
    arene.robot.append(robot)
    window = Window(arene = arene, width = 1000, height = 600, caption = 'Robot 2I013')
    window.start()
    arene.start()
    #img = Image.open(robot.get_image())

tps = 100

ctrc.start()
i = 0
while ctrc.stop():
    ctrc.step()
    time.sleep(1/tps)
    print(robot.x, robot.y, robot.z, robot.vd, robot.vg)

print("stop")

