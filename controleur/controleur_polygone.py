#from composant import Robot, ObjetPhysique
#from code import Terrain, Affichage
from strategie import StratAvanceplus,StratStop,StratTourneplus
from threading import Thread
from math import pi
import time

class Controleur_polygone():
    def __init__(self,rob, cote, dst = 1000,vit = 500):
        self.robot = rob
        self.cnt = 0
        self.Go = None
        self.vitesse = vit
        self.dst = dst
        self.cote = cote

    def start(self):    
        self.Go = StratAvanceplus(self.robot,(self.dst/self.cote),self.vitesse)
        self.Go.start()
        self.cnt = 0
        
    def step(self):
        self.Go.step()
        
        if (self.Go.stop()):
            print(type(self.Go).__name__)
            if (type(self.Go).__name__ == "StratAvanceplus") :#switch strategie
                angle = ((self.cote - 2)*pi)/self.cote
                angle = 180-((angle*180)/pi)
                self.Go = StratTourneplus(self.robot,angle,100)
                self.cnt +=1
                
            elif (type(self.Go).__name__ == 'StratTourneplus') :#switch strategie
                self.Go = StratAvanceplus(self.robot,(self.dst/self.cote),self.vitesse)
        
            self.Go.start()
          
    def stop(self):
        if (self.cnt >= self.cote):
            self.Go = StratStop(self.robot)
            self.Go.start()
            return False
        return True
