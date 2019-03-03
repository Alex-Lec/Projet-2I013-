from composant import*
from principal import*

arene = Terrain()
arene.objet.append(ObjetPhysique(50, 40, 0, 40, 10))
arene.objet.append(ObjetPhysique(100, 100, 0, 10, 100, 10))
arene.objet.append(ObjetPhysique(780, 250, 0, 30, 30))

strategie1 = TrajectoireCarre(arene, 200)
strategie2 = EviterObstacle(arene, 50)

robot1 = Robot(500, 200, 0, arene, strategie1)
robot2 = Robot(400, 400, 0, arene, strategie2)
arene.robot.append(robot1)
arene.robot.append(robot2)
strategie1.appliquer(robot1)
strategie2.appliquer(robot2)

fenetre = Fenetre(arene)

while(true):
    robot1.strategie.update()
    robot2.strategie.update()