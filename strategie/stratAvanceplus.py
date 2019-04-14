import time
from .stratAvance import StratAvance
class StratAvanceplus(StratAvance):
    def __init__(self, robot, distance, vitesse):
        StratAvance.__init__(self,robot,distance,vitesse)
        self.ralenti = 0
    
    def step(self):
        angleg = (self.robot.get_motor_position()[0]*self.robot.WHEEL_CIRCUMFERENCE)/360
        angled = (self.robot.get_motor_position()[1]*self.robot.WHEEL_CIRCUMFERENCE)/360
        
        super().step()
        if(self.ralenti == 0 and (angleg >= self.dst*(4/5) or angled >= self.dst*(4/5))):
            self.robot.set_motor_dps(1, (self.vit/2))
            self.robot.set_motor_dps(2, (self.vit/2))
            self.vit = (self.vit/2)
            self.ralenti = 1
            
        if(self.ralenti == 1 and (angleg >= self.dst*(5/6) or angled >= self.dst*(5/6))):
            self.robot.set_motor_dps(1, (self.vit/2))
            self.robot.set_motor_dps(2, (self.vit/2))
            self.vit = (self.vit/2)
            self.ralenti = 2
        
