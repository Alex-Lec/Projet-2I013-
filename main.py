#!/usr/bin/env python3
# -*- coding: utf-8 -*

from composant import *
from principal import *
import time
from diver import *

arene = Terrain()
robot = Robot(100, 200, 0, arene)
ctrc = Controleur_carre(robot)
arene.robot.append(robot)

affichage = Affichage(arene)
affichage.start()
arene.start()
tps = 25

ctrc.start()
print(robot.get_motor_position())
i = 0
while ctrc.stop():
    ctrc.step()
    time.sleep(1/tps)

print("stop")
