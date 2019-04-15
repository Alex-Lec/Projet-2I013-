#!/usr/bin/env python3
# -*- coding: utf-8 -*

#from composant import Robot, ObjetPhysique
#from code import Terrain, Affichage
from strategie import StratAvanceplus,StratStop,StratTourneplus
from threading import Thread
import time

class Controleur_triangle():
    def __init__(self,rob,dst = 100,vit = 500):
        self.robot = rob
        self.cnt = 0
        self.Go = None
        self.vitesse = vit
        self.dst = dst

    def start(self):
        self.Go = StratAvanceplus(self.robot,self.dst,self.vitesse)
        self.Go.start()
        self.cnt = 0

    def step(self):
        self.Go.step()

        if (self.Go.stop()):
            print(type(self.Go).__name__)
            if (type(self.Go).__name__ == "StratAvanceplus") :#switch strategie
                self.Go = StratTourneplus(self.robot,120,100)
                self.cnt +=1

            elif (type(self.Go).__name__ == 'StratTourneplus') :#switch strategie
                self.Go = StratAvanceplus(self.robot,self.dst,self.vitesse)

            self.Go.start()

    def stop(self):
        if (self.cnt >= 3):
            self.Go = StratStop(self.robot)
            self.Go.start()
            return False
        return True