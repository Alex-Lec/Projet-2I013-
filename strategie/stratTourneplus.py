import time
from .stratTourne import StratTourne

class StratTourneplus(StratTourne):
    def __init__(self, robot, angle, vitesse):
        StratTourne.__init__(self,robot,angle,vitesse)
        self.ralenti = 0
        
    def step(self):
        angleg = (self.robot.get_motor_position()[0]*self.robot.WHEEL_CIRCUMFERENCE) /(self.robot.WHEEL_BASE_CIRCUMFERENCE)
        angled = (self.robot.get_motor_position()[1]*self.robot.WHEEL_CIRCUMFERENCE) /(self.robot.WHEEL_BASE_CIRCUMFERENCE)
        
        super().step()
        if(self.ralenti == 0 and (angleg >= self.angle*(4/5) or angled <= -self.angle*(4/5))):
            self.robot.set_motor_dps(1,  (self.vit/2))
            self.robot.set_motor_dps(2, -(self.vit/2))
            self.vit = (self.vit/2)
            self.ralenti = 1
            
        if(self.ralenti == 1 and (angleg >= self.angle*(5/6) or angled <= -self.angle*(5/6))):
            self.robot.set_motor_dps(1,  (self.vit/2))
            self.robot.set_motor_dps(2, -(self.vit/2))
            self.vit = (self.vit/2)
            self.ralenti = 2
            
