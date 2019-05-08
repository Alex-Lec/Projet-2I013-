#!/usr/bin/env python3
# -- coding: utf-8 -

from strategie import StratAvance, StratStop, StratTourne, StratTraitementImage
from threading import Thread
from composant import vecteur
import time
import math
import numpy as np
import cv2 as cv
import sys

class Controleur_balise():
    def __init__(self, rob, dst = 100, vit = 500):
        self.robot = rob
        self.Go = None
        self.cnt = 2
        self.dst = dst
        self.vitesse = vit

    def start(self):

        self.Go = StratTraitementImage(self.robot)
        self.distance_pixels = self.Go.start()

        self.Go = StratTourne(self.robot, self.distance_pixels / 10, 500)
        self.Go.start()

        """
        self.Go = StratAvance(self.robot, 100, self.vitesse)
        self.Go.start()
        self.cnt = 2
        """

    def step(self):

        self.Go.step()

        self.Go = StratTraitementImage(self.robot)
        self.distance_pixels = self.Go.start()

        self.Go = StratTourne(self.robot, self.distance_pixels / 10, 500)
        self.Go.start()

        """
        self.Go.step()
        
        if (self.robot.get_distance() <= self.dst):
            if (self.cnt != 0):
                self.Go = StratStop(self.robot)
                self.Go.start()
                self.cnt = 0
        
        elif (self.robot.get_distance() <= (2*self.dst)):
            if (self.cnt == 0):
                self.Go = StratAvance(self.robot, 100, self.vitesse/2)
                self.Go.start()
                self.cnt = 2
        
            elif (self.cnt != 1):
                self.Go.update(self.vitesse/2)
                self.cnt = 1
        
        elif (self.cnt != 2 ):
            self.Go = StratAvance(self.robot, 100, self.vitesse)
            self.Go.start()
            self.cnt = 2

        if (self.cnt == 0):
        """

    def stop(self):

        if (self.cnt == 0):
            return False
        return True

        """
        if (self.cnt == 0):
            return False
        return True 
        """