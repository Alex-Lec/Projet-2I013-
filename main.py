#!/usr/bin/env python3
# -*- coding: utf-8 -*

import time
from diver import *
from controleur import Controleur_carre, Controleur_droit_stop, Controleur_image, Controleur_triangle, Controleur_cercle, \
    Controleur_polygone_n_cotes, Controleur_zones_grises
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
    """
    arene.objet.append(ObjetPhysique(100, 20, 0, 50, 100, 100))
    arene.objet.append(ObjetPhysique(20, 100, 0, 100, 50, 100))
    arene.objet.append(ObjetPhysique(1300, 100, 15, 80, 70, 100))
    arene.objet.append(ObjetPhysique(500, 500, 10, 100, 100, 10))
    arene.objet.append(ObjetPhysique(780, 250, 0, 100, 50, 100))
    """

###################################################################

print("\n\
               Bienvenue dans la matrice\n\
               Selectionnez votre choix\n\n\
            #  Controleur_carre             -> 1 #\n\
            #  Controleur_droit_stop        -> 2 #\n\
            #  Controleur_detection_carre   -> 3 #\n\
            #  Controleur_balise            -> 4 #\n\
            #  Controleur_image             -> 5 #\n\
            #  Controleur_triangle          -> 6 #\n\
            #  Controleur_polygones_n_cotes -> 7 #\n\
            #  Controleur_zones_grises      -> 8 #\n\
            #  Quit                         -> Q #")

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

elif (choix == "6"):
    ctrc = Controleur_triangle(robot)

elif (choix == "7"):
    ctrc = Controleur_polygone_n_cotes(robot, nb_cotes = 20)

elif (choix =="8"):
    ctrc = Controleur_zones_grises(robot)

    arene.zones_grises.append(Zones_Grises(300, 25, 0, 50, 50, 50))
    arene.zones_grises.append(Zones_Grises(300, 80, 0, 50, 50, 50))
    arene.zones_grises.append(Zones_Grises(300, 135, 0, 50, 50, 50))

    arene.zones_grises.append(Zones_Grises(300, 325, 0, 50, 50, 50))
    arene.zones_grises.append(Zones_Grises(300, 380, 0, 50, 50, 50))
    arene.zones_grises.append(Zones_Grises(300, 435, 0, 50, 50, 50))

    arene.zones_grises.append(Zones_Grises(600, 135, 0, 50, 50, 50))
    arene.zones_grises.append(Zones_Grises(600, 190, 0, 50, 50, 50))
    arene.zones_grises.append(Zones_Grises(600, 245, 0, 50, 50, 50))

    arene.zones_grises.append(Zones_Grises(600, 425, 0, 50, 50, 50))
    arene.zones_grises.append(Zones_Grises(600, 480, 0, 50, 50, 50))
    arene.zones_grises.append(Zones_Grises(600, 535, 0, 50, 50, 50))

    arene.zones_grises.append(Zones_Grises(900, 25, 0, 50, 50, 50))
    arene.zones_grises.append(Zones_Grises(900, 80, 0, 50, 50, 50))
    arene.zones_grises.append(Zones_Grises(900, 135, 0, 50, 50, 50))

    arene.zones_grises.append(Zones_Grises(900, 225, 0, 50, 50, 50))
    arene.zones_grises.append(Zones_Grises(900, 280, 0, 50, 50, 50))
    arene.zones_grises.append(Zones_Grises(900, 335, 0, 50, 50, 50))

    arene.zones_grises.append(Zones_Grises(1200, 135, 0, 50, 50, 50))
    arene.zones_grises.append(Zones_Grises(1200, 190, 0, 50, 50, 50))
    arene.zones_grises.append(Zones_Grises(1200, 245, 0, 50, 50, 50))

    arene.zones_grises.append(Zones_Grises(1200, 425, 0, 50, 50, 50))
    arene.zones_grises.append(Zones_Grises(1200, 480, 0, 50, 50, 50))
    arene.zones_grises.append(Zones_Grises(1200, 535, 0, 50, 50, 50))

    arene.zones_grises.append(Zones_Grises(1350, 25, 0, 50, 50, 50))

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
