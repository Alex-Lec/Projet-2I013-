import time
from .stratAvance import StratAvance
class StratAvanceprud(StratAvance):
    def __init__(self, robot, dst, vitesse):
        StratAvance.__init__(self,robot,100000,vitesse)
        self.dststop = dst
        self.vitesse = vitesse
        self.etat = 0
        
    def step(self):
        super().step()
        
        if self.robot.get_distance() <= self.dststop*2:
            if self.etat != 1:
                self.robot.set_motor_dps(1, self.vitesse/2)
                self.robot.set_motor_dps(2, self.vitesse/2)
                self.vit = self.vitesse/2
                self.etat = 1
        
        
    def stop(self):
        return self.robot.get_distance() <= self.dststop
