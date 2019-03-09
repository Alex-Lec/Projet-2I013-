from composant import*
from principal import*
import time
from diver import*

arene = Terrain()
robot = Robot(100, 200, 0, arene)
robot.vitesse = 10

arene.robot.append(robot)

print("hop")
affichage = Affichage(arene)
print("flop")
affichage.start()
arene.start()
affichage.fenetre.mainloop()



