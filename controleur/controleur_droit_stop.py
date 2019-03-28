from composant import Robot, ObjetPhysique
from code import Terrain, Affichage
from strategie import StratAvanceStop,StratStop
from threading import Thread
import time;

class Controleur_droit_stop():
    def __init__(self,rob):
        self.robot = rob
        self.Go = None
        self.cnt = 0
    
    
    def start(self):
        self.Go = StratAvanceStop(self.robot,1000,50)
        self.Go.start()
        
    def step(self):
        if(self.cnt == 0 and self.robot.get_distance() <= 100):
            self.robot.set_motor_dps(1, 500)
            self.robot.set_motor_dps(2, 500)
            self.cnt = 1
        
    def stop(self):
        if (self.Go.stop()):
            self.Go = StratStop(self.robot)
            self.Go.start()
            return False
        return True
