import time
class StratAvanceStop:
    def __init__(self, robot, vitesse, dst):
        self.robot = robot
        self.vit = vitesse
        self.dst = dst
    
    def start(self):
        self.robot.set_motor_dps(1 , self.vit)
        self.robot.set_motor_dps(2, self.vit)
        self.robot.offset_motor_encoder(1, self.robot.get_motor_position()[0])
        self.robot.offset_motor_encoder(2, self.robot.get_motor_position()[1])
        #self.robot.last_up = time.time()
    
    def step(self):
        pass
    
    def stop(self):
        if(self.robot.get_distance() <= self.dst):
            return True
        
        return False
