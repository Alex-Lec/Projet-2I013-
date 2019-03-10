import time
class StratStop:
    def __init__(self, robot):
        self.robot = robot

    def start(self):
        self.robot.set_motor_dps("MOTOR_LEFT" , 0)
        self.robot.set_motor_dps("MOTOR_RIGHT", 0)
