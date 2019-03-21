#!/usr/bin/env python3
# -*- coding: utf-8 -*

from composant import *
from principal import *
import time
from diver import *

arene = Terrain()
robot = Robot(100, 100, 0, arene)
ctrc = Controleur_droit_stop(robot)
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
