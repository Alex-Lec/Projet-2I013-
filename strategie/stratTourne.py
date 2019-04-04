import time
class StratTourne:
    def __init__(self, robot, angle, vitesse):
        """
        Tourne d'un angle 0 à la vitesse v; !!! Tourne dans le sens trigo. 
        Un angle < 0 le fait tourner dans le sens anti-trigo 
        
        """
        self.robot = robot
        self.angle = angle
        if(self.angle<0):
            vitesse = -vitesse
        self.vit = vitesse
        
    def start(self):
        self.robot.set_motor_dps(1,  self.vit)
        self.robot.set_motor_dps(2, -self.vit)
        self.robot.offset_motor_encoder(1, self.robot.get_motor_position()[0])
        self.robot.offset_motor_encoder(2, self.robot.get_motor_position()[1])

    def step(self):
        pos1 = self.robot.get_motor_position()[0] 
        pos2 = self.robot.get_motor_position()[1]
    
        if (pos1 < -pos2):
            self.robot.set_motor_dps(1,  self.vit +  (pos1 + pos2))
        
        elif (pos1 > -pos2):
            self.robot.set_motor_dps(2, -self.vit + -(pos2 + pos1))
            
        else :
            self.robot.set_motor_dps(1, self.vit)
            self.robot.set_motor_dps(2, -self.vit)
    
    def stop(self):
        if(((self.robot.get_motor_position()[0]*self.robot.WHEEL_CIRCUMFERENCE /self.robot.WHEEL_BASE_CIRCUMFERENCE) >= self.angle) and((self.robot.get_motor_position()[1]*self.robot.WHEEL_CIRCUMFERENCE /self.robot.WHEEL_BASE_CIRCUMFERENCE) <= -self.angle)):
            return True
        
        return False
