from composant import Robot, ObjetPhysique
from code import Terrain, Affichage
from strategie import StratAvance,StratStop,StratTourne
from threading import Thread
import time;

class Controleur_carre():
    def __init__(self,rob):
        self.robot = rob
        self.cnt = 0
        self.Go = None

    def start(self):    
        self.Go = StratAvance(self.robot,500,500)
        self.Go.start()
        self.cnt = 0
        
    def step(self):
        if (self.Go.stop()):
            print(type(self.Go).__name__)
            if (type(self.Go).__name__ == "StratAvance") :#switch strategie
                self.Go = StratTourne(self.robot,90,100)
                self.cnt +=1
            elif (type(self.Go).__name__ == 'StratTourne') :#switch strategie
                self.Go = StratAvance(self.robot,500,500)
        
            self.Go.start()
        
    def stop(self):
        if (self.cnt >= 4):
            self.Go = StratStop(self.robot)
            self.Go.start()
            return False
        return True
