from composant import Robot, ObjetPhysique
from principal import Terrain, Affichage
from threading import Thread
import time;

class Controleur(Thread):
    def __init__(self):
        super(Controleur,self).__init__()
        self.robot
        

    def run(self):
        while True:
         self.update()
        #time.sleep(1./fps)
"""
while (True):
    if len(rob.event) == 0 or 
        rob.event[-1][0] ="tourner" and rob.event[-1][1] >= time.time + 4 :
        
        set_motor_dps(MOTOR_LEFT, 90)
        set_motor_dps(MOTOR_RIGHT, 90)
        event.append(("avancer",time.time()))
        
        
    if rob.event[-1][0] = "avancer" and rob.event[-1][1] >= time.time + 4 :
        set_motor_dps(MOTOR_LEFT, 90)
        set_motor_dps(MOTOR_RIGHT, -90)
        event +=[("tourner",time.time())]
    
    
    rob.update()
    fenetre.update()
    """
