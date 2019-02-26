from composant import Robot, ObjetPhysique
from .terrain import Terrain
from .fenetre import Fenetre
import time;

arene = Terrain()
rob = Robot(100,100,0)
arene.robot.append(rob)
t = time.time()
fenetre = Fenetre(arene)

while (True):
    """
    if len(rob.event) == 0 or 
        rob.event[-1][0] ="tourner" and rob.event[-1][1] >= time.time + 4 :
        
        set_motor_dps(MOTOR_LEFT, 90)
        set_motor_dps(MOTOR_RIGHT, 90)
        rob.event.append(("avancer",time.time()))
        
        
    if rob.event[-1][0] = "avancer" and rob.event[-1][1] >= time.time + 4 :
        set_motor_dps(MOTOR_LEFT, 90)
        set_motor_dps(MOTOR_RIGHT, -90)
        rbo.event +=[("tourner",time.time())]
    
    
    rob.update()
    fenetre.update()
    """
