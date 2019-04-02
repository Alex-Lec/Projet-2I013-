#!/usr/bin/env python3
# -*- coding: utf-8 -*

from composant import *
from code import *
import time
from diver import *
from controleur import Controleur_carre, Controleur_droit_stop
import sys
arene = Terrain()
robot = Robot(100, 100, 0, arene)


###################################################################
print("\
              Bienvenue dans la matrice\n\
              Selectionnez votre choix\n\n\
            #  Controleur_carre      -> 1 #\n\
            #  Controleur_droit_stop -> 2 #\n\
            #  quit                  -> q #")

choix = input()
if (choix == "1"):
    ctrc = Controleur_carre(robot)
elif (choix == "2"):
    ctrc = Controleur_droit_stop(robot)
else :
    sys.exit()

###################################################################

arene.robot.append(robot)
affichage = Affichage(arene)
affichage.start()
arene.start()
tps = 100

ctrc.start()
i = 0
while ctrc.stop():
    ctrc.step()
    time.sleep(1/tps)

print("stop")

