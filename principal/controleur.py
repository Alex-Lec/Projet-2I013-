from composant import Robot, ObjetPhysique
from principal import Terrain, Affichage
from strategie import StratAvance,StratStop,StratTourne
from threading import Thread
import time;

class Controleur(Thread):
    def __init__(self,rob):
        super(Controleur,self).__init__()
        self.robot = rob
        self.fps = 25

    def run(self):
        Go   = StratAvance(self.robot,100,200)
        Go.start()
        cnt = 0
        while True:
            if (Go.stop()):
                print(type(Go).__name__)
                if (type(Go).__name__ == "StratAvance") :
                    Go = StratTourne(self.robot,90,25)
                    cnt +=1
                    
                elif (type(Go).__name__ == 'StratTourne') :
                    Go = StratAvance(self.robot,100,200)
                
                Go.start()
            
            if (cnt == 4):
                break
            time.sleep(1./self.fps)
        
        Go = StratStop(self.robot)
        Go.start()
