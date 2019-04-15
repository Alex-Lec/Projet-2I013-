#!/usr/bin/env python3
# -*- coding: utf-8 -*

from strategie import StratAvanceplus,StratStop,StratTourneplus
from threading import Thread
import time
import math

class Controleur_polygone_n_cotes():
    def __init__(self, rob, dst = 300, vit = 500, nb_cotes = 4):
        self.robot = rob
        self.cnt = 0
        self.Go = None
        self.vitesse = vit
        self.dst = 300 / nb_cotes
        self.nb_cotes = nb_cotes
        self.angle = 180 - math.degrees(((nb_cotes - 2) * math.pi) / nb_cotes)

    def start(self):
        self.Go = StratAvanceplus(self.robot, self.dst, self.vitesse)
        self.Go.start()
        self.cnt = 0

    def step(self):
        self.Go.step()

        if (self.Go.stop()):
            print(type(self.Go).__name__)
            if (type(self.Go).__name__ == "StratAvanceplus") :#switch strategie
                self.Go = StratTourneplus(self.robot, self.angle, 100)
                print(self.angle)
                self.cnt +=1
                
            elif (type(self.Go).__name__ == 'StratTourneplus') :#switch strategie
                self.Go = StratAvanceplus(self.robot,self.dst,self.vitesse)
        
            self.Go.start()

    def stop(self):
        if (self.cnt >= self.nb_cotes):
            self.Go = StratStop(self.robot)
            self.Go.start()
            return False
        return True