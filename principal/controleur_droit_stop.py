from composant import Robot, ObjetPhysique
from principal import Terrain, Affichage
from strategie import StratAvanceStop,StratStop
from threading import Thread
import time;

class Controleur_droit_stop():
    def __init__(self,rob):
        self.robot = rob
        self.Go = None
    
    def start(self):
        self.Go = StratAvanceStop(self.robot,50,200)
        self.Go.start()
        
    def step(self):
        pass
        
    def stop(self):
        if (self.Go.stop()):
            self.Go = StratStop(self.robot)
            self.Go.start()
            return False
        return True
