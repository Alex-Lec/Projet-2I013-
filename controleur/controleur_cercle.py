#!/usr/bin/env python3
# -*- coding: utf-8 -*

#from composant import Robot, ObjetPhysique
#from code import Terrain, Affichage
from strategie import StratAvanceplus,StratStop,StratTourneplus
from threading import Thread
import time

class Controleur_cercle():
    def __init__(self, rob, dst = 500, vit = 500):
        self.robot = rob
        self.dst = dst
        self.vit = vit
        self.cnt = 0
        self.Go = None

    def start(self):
        pass

    def step(self):
        pass

    def stop(self):
        pass
