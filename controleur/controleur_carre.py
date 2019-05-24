#from composant import Robot, ObjetPhysique
#from code import Terrain, Affichage
from strategie import StratAvanceplus,StratStop,StratTourneplus
from threading import Thread

class Controleur_carre():

    def __init__(self,rob,dst = 500,vit = 500):
        self.robot = rob
        self.cnt = 0 # compteur du nombre de côté fait
        self.Go = None
        self.vitesse = vit
        self.dst = dst

    def start(self):    
        self.Go = StratAvanceplus(self.robot,self.dst,self.vitesse)
        self.Go.start()
        
    def step(self):
        self.Go.step()
        
        # Fin de strategie si angle de 90 ou distance supérieur à self.dst
        if (self.Go.stop()):
            print(type(self.Go).__name__)
            if (type(self.Go).__name__ == "StratAvanceplus") :#switch strategie
                self.Go = StratTourneplus(self.robot,90,100)
                self.cnt +=1 # On à fait un coté de plus
                
            elif (type(self.Go).__name__ == 'StratTourneplus') :#switch strategie
                self.Go = StratAvanceplus(self.robot,self.dst,self.vitesse)
        
            self.Go.start()
          
    def stop(self):
        
        # Si les 4 côtés du carré on été effectués on stop le robot
        if (self.cnt >= 4):
            self.Go = StratStop(self.robot)
            self.Go.start()
            return False
        return True
