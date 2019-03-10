import time
class StratAvance:
    def __init__(self, robot, distance, vitesse):
        self.robot = robot
        self.dst = distance
        self.vit = vitesse
    
    def start(self):
        self.robot.set_motor_dps("MOTOR_LEFT" , self.vit)
        self.robot.set_motor_dps("MOTOR_RIGHT", self.vit)
        self.robot.offset_motor_encoder("MOTOR_LEFT_RIGHT", 0)
        self.robot.last_up = time.time()
        
    def stop(self):
        if((self.robot.get_motor_position()[0]*self.robot.WHEEL_CIRCUMFERENCE)
            /360 > self.dst):
            return True
            
        if((self.robot.get_motor_position()[1]*self.robot.WHEEL_CIRCUMFERENCE)
            /360 > self.dst):
            return True
        
        return False
