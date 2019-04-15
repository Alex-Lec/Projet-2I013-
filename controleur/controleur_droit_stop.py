from strategie import StratAvanceprud, StratStop
import time;

class Controleur_droit_stop():
    def __init__(self,rob, dst = 100, vit = 1000):
        self.robot = rob
        self.Go = None
        self.dst = dst
        self.vitesse = vit
    
    def start(self):
        self.Go = StratAvanceprud(self.robot, self.dst, self.vitesse)
        self.Go.start()
        
    def step(self):
        self.Go.step()
        
        if(self.Go.stop()):
            if(type(self.Go).__name__ != "StratStop"):
                self.Go = StratStop(self.robot)
                self.Go.start()
                
            if(self.robot.get_distance() >= self.dst):
                self.Go = StratAvanceprud(self.robot, self.dst, self.vitesse)
                self.Go.start()
                
        
    def stop(self):
        return True
