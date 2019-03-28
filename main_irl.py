#!/usr/bin/env python3
# -*- coding: utf-8 -*

import time
from diver import *
from controleur import Controleur_carre, Controleur_droit_stop
import sys
from robot2I013.robot2I013 import Robot2I013
#arene = Terrain()
robot = Robot2I013()


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

#arene.robot.append(robot)
#affichage = Affichage(arene)
#affichage.start()
#arene.start()
tps = 100

ctrc.start()
i = 0
while ctrc.stop():
    ctrc.step()
    time.sleep(1/tps)

print("stop")

