import time
from .stratAvance import StratAvance
class StratAvanceplus(StratAvance):
    def __init__(self, robot, distance, vitesse, diff = 0):
        StratAvance.__init__(self,robot,distance,vitesse,diff)
    
    def update(self, vitesse):
        self.robot.set_motor_dps(1, vitesse)
        self.robot.set_motor_dps(2, vitesse)
        self.vit = vitesse
