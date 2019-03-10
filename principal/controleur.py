from composant import Robot, ObjetPhysique
from principal import Terrain, Affichage
from .strategie import Strategie
from threading import Thread
import time;

class Controleur(Thread):
    def __init__(self,rob):
        super(Controleur,self).__init__()
        self.robot = rob
        self.fps = 10
        self.strategie = Strategie(rob)
        

    def run(self):
        while True:
            self.update()
            time.sleep(1./self.fps)


    def update(self):
        #for i in range(4):
        self.strategie.avancer(200,50)
        #Strategie.tourner(90 ,50)
