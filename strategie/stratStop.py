import time
class StratStop:
    def __init__(self, robot):
        self.robot = robot
        
    def step(self):
        pass

    def start(self):
        self.robot.set_motor_dps(1 , 0)
        self.robot.set_motor_dps(2 , 0)
