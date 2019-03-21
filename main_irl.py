#!/usr/bin/env python3
# -*- coding: utf-8 -*

from composant import *
from principal import *
import time
from diver import *
from robot2I013.robot2I013 import Robot2I013

robot = Robot2I013()
ctrc = Controleur_carre(robot)

tps = 30

ctrc.start()
print(robot.get_motor_position())
i = 0
while ctrc.stop():
    ctrc.step()
    time.sleep(1/tps)

print("stop")
