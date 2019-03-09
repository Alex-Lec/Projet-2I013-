from composant import*
from principal import*
import time
from diver import*

arene = Terrain()
robot = Robot(100, 200, 0, arene)
arene.robot.append(robot)
print("hop")
affichage = Affichage(arene)
print("flop")
affichage.start()
affichage.fenetre.mainloop()
arene.start()


