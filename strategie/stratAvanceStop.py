import time
class StratAvanceStop:
    def __init__(self, robot, distance, vitesse):
        self.robot = robot
        self.vit = vitesse
        self.dst = distance
    
    def start(self):
        self.robot.set_motor_dps(1 , self.vit)
        self.robot.set_motor_dps(2, self.vit)
        self.robot.offset_motor_encoder(1, self.robot.get_motor_position()[0])
        self.robot.offset_motor_encoder(2, self.robot.get_motor_position()[1])
    
    def step(self):
        pos1 =self.robot.get_motor_position()[0] 
        pos2 = self.robot.get_motor_position()[1]
        
        if (pos1 < pos2):
            self.robot.set_motor_dps(1, self.vit + 2*(pos2 - pos1))
        
        elif (pos1 > pos2):
            self.robot.set_motor_dps(2, self.vit + 2*(pos1 - pos2))
            
        else :
            self.robot.set_motor_dps(1, self.vit)
            self.robot.set_motor_dps(2, self.vit)
    
    def stop(self):
        if(self.robot.get_distance() <= self.dst):
            return True
        
        return False
