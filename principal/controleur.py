from composant import Robot, ObjetPhysique
from principal import Terrain, Affichage
from threading import Thread
import time;

class Controleur(Thread):
    def __init__(self):
        super(Controleur,self).__init__()
        self.robot
        self.fps
        

    def run(self):
        while True:
            self.update()
            time.sleep(1./fps)


    def update(self):
        for i in range(4):
            Strategie.avancer(100)
            Strategie.tourner(90)
        
