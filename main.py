from composant import*
from principal import*
import time
from diver import*

arene = Terrain()
robot = Robot(100, 200, 0, arene)
robot.MOTOR_LEFT = 50
robot.MOTOR_RIGHT = 50

arene.robot.append(robot)
affichage = Affichage(arene)
affichage.start()
arene.start()
affichage.fenetre.mainloop()



