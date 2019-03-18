#!/usr/bin/env python3
# -*- coding: utf-8 -*

from composant import *
from principal import *
import time
from diver import *

arene = Terrain()
robot = Robot(100, 200, 0, arene)
controleur = Controleur(robot)
arene.robot.append(robot)

affichage = Affichage(arene)
affichage.start()
arene.start()
controleur.start()
affichage.fenetre.mainloop()



