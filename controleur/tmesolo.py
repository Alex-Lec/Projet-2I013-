#!/usr/bin/env python3
# -- coding: utf-8 -

from strategie import StratAvanceplus,StratStop,StratTourneplus,StratAvance
from threading import Thread
import time

#Question 2.1
class Controleur_triangle():
    def __init__(self,rob,dst = 500,vit = 500):
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


#Question 2.2
class Controleur_polygone():
    def __init__(self,rob,n,dst = 1500,vit = 500):
        self.robot = rob
        self.cnt = 0
        self.Go = None
        self.vitesse = vit
        self.dst = dst/n
        self.n = n

    def start(self):
        self.Go = StratAvanceplus(self.robot,self.dst,self.vitesse)
        self.Go.start()
        self.cnt = 0

    def step(self):
        self.Go.step()

        if (self.Go.stop()):
            print(type(self.Go).__name__)
            if (type(self.Go).__name__ == "StratAvanceplus") :#switch strategie
                angle =180 - ((self.n-2)*180)/self.n
                self.Go = StratTourneplus(self.robot,angle,100)
                self.cnt +=1

            elif (type(self.Go).__name__ == 'StratTourneplus') :#switch strategie
                self.Go = StratAvanceplus(self.robot,self.dst,self.vitesse)

            self.Go.start()

    def stop(self):
        if (self.cnt >= self.n):
            self.Go = StratStop(self.robot)
            self.Go.start()
            return False
        return True

#Question 2.3
class Controleur_arene():
    def __init__(self,rob, dst = 250, vit = 1000):
        self.robot = rob
        self.Go = None
        self.dst = dst
        self.vitesse = vit

    def start(self):
        self.Go = StratAvanceplus(self.robot, self.dst, self.vitesse)
        self.Go.start()

    def step(self):
        self.Go.step()

        if(self.Go.stop()):
            if(type(self.Go).__name__ != "StratStop"):
                self.Go = StratTourneplus(self.robot,90,100)
                self.Go.start()

            if(self.robot.get_distance() >= self.dst):
                self.Go = StratAvanceplus(self.robot, self.dst, self.vitesse)
                self.Go.start()


    def stop(self):
        return True
