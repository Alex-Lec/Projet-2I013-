import time
class StratAvance:
    def __init__(self, robot, distance, vitesse):
        self.robot = robot
        self.dst = distance
        self.vit = vitesse
    
    def start(self):
        self.robot.set_motor_dps(1, self.vit)
        self.robot.set_motor_dps(2, self.vit)
        self.robot.offset_motor_encoder(1, self.robot.get_motor_position()[0])
        self.robot.offset_motor_encoder(2, self.robot.get_motor_position()[1])
        #self.robot.last_up = time.time()
    
    def step(self):
        pos1 =self.robot.get_motor_position()[0] 
        pos2 = self.robot.get_motor_position()[1]
        if (pos1 > pos2):
            print("declage gauche")
            self.robot.set_motor_dps(1, self.vit + pos1 - pos2)
        if (pos1 < pos2):
            print("declage droit")
            self.robot.set_motor_dps(2, self.vit + pos1 - pos2)
        if (pos1 == pos2):
            self.robot.set_motor_dps(1, self.vit)
            self.robot.set_motor_dps(2, self.vit)
            
        print("Success")
    
    def stop(self):
        if((self.robot.get_motor_position()[0]*self.robot.WHEEL_CIRCUMFERENCE)
            /360 > self.dst):
            return True
            
        if((self.robot.get_motor_position()[1]*self.robot.WHEEL_CIRCUMFERENCE)
            /360 > self.dst):
            return True
        
        return False
