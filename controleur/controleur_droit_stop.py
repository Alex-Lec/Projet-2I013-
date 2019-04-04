#from composant import Robot, ObjetPhysique
#from code import Terrain, Affichage
from strategie import StratAvance,StratStop
from threading import Thread
import time;

class Controleur_droit_stop():
    def __init__(self,rob, dst = 100, vit = 1000):
        self.robot = rob
        self.Go = None
        self.cnt = 2
        self.dst = dst
        self.vitesse = vit
    
    def start(self):
        self.Go = StratAvance(self.robot, 100, self.vitesse)
        self.Go.start()
        self.cnt = 2
        
    def step(self):
        self.Go.step()
        
        if(self.robot.get_distance() <= self.dst):
            if (self.cnt != 0):
                self.Go = StratStop(self.robot)
                self.Go.start()
                self.cnt = 0
        
        elif(self.robot.get_distance() <= (2*self.dst)):
            if (self.cnt == 0):
                self.Go = StratAvance(self.robot, 100, self.vitesse/2)
                self.Go.start()
                self.cnt = 2
        
            elif (self.cnt != 1):
                self.Go.update(self.vitesse/2)
                self.cnt = 1
        
        elif(self.cnt != 2 ):
            self.Go = StratAvance(self.robot, 100, self.vitesse)
            self.Go.start()
            self.cnt = 2
        
        
    def stop(self):
        #if (self.Go.stop()):
        #    self.Go = StratStop(self.robot)
        #    self.Go.start()
        #    return False
        return True
