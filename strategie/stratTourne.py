import time
class StratTourne:
    def __init__(self, robot, angle, vitesse):
        self.robot = robot
        self.angle = angle
        self.vit = vitesse

    def start(self):
        self.robot.set_motor_dps(1,  self.vit)
        self.robot.set_motor_dps(2, -self.vit)
        self.robot.offset_motor_encoder(1, self.robot.get_motor_position()[0])
        self.robot.offset_motor_encoder(2, self.robot.get_motor_position()[1])
        self.robot.last_up = time.time()
    
    def stop(self):        
        if((2*self.robot.get_motor_position()[0]*self.robot.WHEEL_CIRCUMFERENCE /self.robot.WHEEL_BASE_CIRCUMFERENCE) 
                >= self.angle):
            return True
            
        if((2*self.robot.get_motor_position()[1]*self.robot.WHEEL_CIRCUMFERENCE /self.robot.WHEEL_BASE_CIRCUMFERENCE)
                <= -self.angle):
            return True
        
        return False
