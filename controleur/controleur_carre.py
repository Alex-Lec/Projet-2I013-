#from composant import Robot, ObjetPhysique
#from code import Terrain, Affichage
from strategie import StratAvance,StratStop,StratTourne
from threading import Thread
import time

class Controleur_carre():
    def __init__(self,rob,dst = 500,vit = 500):
        self.robot = rob
        self.cnt = 0
        self.Go = None
        self.vitesse = vit
        self.dst = dst

    def start(self):    
        self.Go = StratAvance(self.robot,self.dst,self.vitesse)
        self.Go.start()
        self.cnt = 0
        
    def step(self):
        self.Go.step()
        if (self.Go.stop()):
            print(type(self.Go).__name__)
            if (type(self.Go).__name__ == "StratAvance") :#switch strategie
                self.Go = StratTourne(self.robot,90,100)
                self.cnt +=1
                
            elif (type(self.Go).__name__ == 'StratTourne') :#switch strategie
                self.Go = StratAvance(self.robot,self.dst,self.vitesse)
        
            self.Go.start()
          
    def stop(self):
        if (self.cnt >= 4):
            self.Go = StratStop(self.robot)
            self.Go.start()
            return False
        return True
