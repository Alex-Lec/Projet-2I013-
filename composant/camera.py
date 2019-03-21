#!/usr/bin/env python3
# -*- coding: utf-8 -*

class Camera:
    
    def __init__(self, robot, terrain):
        self.robot = robot
        self.terrain = terrain
    
    def marqueur(self):
        #A definir plus tard : Renvoie true si un des marqueurs est dans le
        #champ de vision du robot, false sinon
        return