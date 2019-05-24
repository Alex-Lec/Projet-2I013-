
from .stratAvance import StratAvance
class StratAvanceprud(StratAvance):
    """
    Cette stratégie permet de ralentir ou d'arrêter le robot en fonction de la distance
    que celui-ci mesure avec son capteur.
    """

    def __init__(self, robot, dst, vitesse):
        StratAvance.__init__(self,robot,100000,vitesse)
        self.dststop = dst
        self.vitesse = vitesse
        self.etat = 0
        
    def step(self):
        super().step()
        
        # On ralentie le robot s'il se trouve à 2 fois la distance d'arrêt
        if self.robot.get_distance() <= self.dststop*2:
            if self.etat != 1:
                self.robot.set_motor_dps(1, self.vitesse/2)
                self.robot.set_motor_dps(2, self.vitesse/2)
                self.vit = self.vitesse/2
                self.etat = 1
        
        
    def stop(self):
        # Fin si le robot se trouve à ou au-dela de la distance d'arrêt.
        return self.robot.get_distance() <= self.dststop
