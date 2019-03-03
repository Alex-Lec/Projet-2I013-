#!/usr/bin/env python3
# -- coding: utf-8 -

from principal import Terrain
from composant import Robot, ObjetPhysique

class Strategie:

    def __init__(self, arene, robot):
        self.arene = arene
        self.robot = robot

class EviterObstacle(Strategie):
    def __init__(self, arene, robot, DISTANCE_SECURITE = 50):
        Strategie.__init__(self, arene, robot)
        self.DISTANCE_SECURITE = DISTANCE_SECURITE
    
    def update(self):
        while (self.robot.get_distance() < DISTANCE_SECURITE) :
            self.arene.tourner_robot_d(robot)
        self.arene.avancer_robot(robot)

class TrajectoireCarre(Strategie):

    def __init(self, arene, robot, COTE_CARRE = 200):
        Strategie.__init__(self, arene, robot)
        self.COTE_CARRE = COTE_CARRE

    def update(self):
        distance_parcourue = 0
        while (distance_parcourue < COTE_CARRE):
            self.arene.avancer_robot(robot)
        self.robot.scalaire_rotation = 90
        self.robot.update()