from strategie import StratAvanceprud, StratStop, StratTourneplus
import time;

class Controleur_tour():
    def __init__(self,rob, dst = 50, vit = 500):
        self.robot = rob
        self.Go = None
        self.dst = dst
        self.vitesse = vit
        self.cnt = 0
    
    def start(self):
        self.Go = StratAvanceprud(self.robot, self.dst, self.vitesse)
        self.Go.start()
        
    def step(self):
        self.Go.step()
        
        if(self.Go.stop()):
            if(type(self.Go).__name__ != "StratTourneplus"):
                self.Go = StratTourneplus(self.robot, 90, 50)
                self.Go.start()
                self.cnt += 1
                
            if(self.robot.get_distance() >= self.dst):
                self.Go = StratAvanceprud(self.robot, self.dst, self.vitesse)
                self.Go.start()
                
        
    def stop(self):
        if(self.cnt >= 4):
            return False
        return True
