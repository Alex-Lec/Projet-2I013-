from composant import Robot, ObjetPhysique
import time
from math import pi

class Strategie:
    def __init__(self, robot):
        self.robot = robot
        self.stop = False
    
    def avancer(self,dst, vit):
        self.robot.offset_motor_encoder("MOTOR_LEFT_RIGHT", 0)
        self.robot.set_motor_dps("MOTOR_LEFT", vit)
        self.robot.set_motor_dps("MOTOR_RIGHT", vit)
        
        while(self.stop != True):
            if(self.robot.get_motor_position()[0] * self.robot.WHEEL_CIRCUMFERENCE > dst):
                self.stop = True
                break
            if(self.robot.get_motor_position()[1] * self.robot.WHEEL_CIRCUMFERENCE > dst):
                self.stop = True
                break
        
    
    def reculer(self,dst, vit):
        self.robot.offset_motor_encoder(MOTOR_LEFT_RIGHT, 0)
        self.robot.set_motor_dps(MOTOR_LEFT, -vit)
        self.robot.set_motor_dps(MOTOR_RIGHT, -vit)
        
        while(True):
            if(self.robot.get_motor_position[0] * self.robot.WHEEL_CIRCUMFERENCE > -dst):
                break
            if(self.robot.get_motor_position[1] * self.robot.WHEEL_CIRCUMFERENCE > -dst):
                break
    
    def tourner(self,angle, vit):
        self.robot.offset_motor_encoder(MOTOR_LEFT_RIGHT, 0)
        if (angle > 0):
            self.robot.set_motor_dps(MOTOR_LEFT, vit)
            self.robot.set_motor_dps(MOTOR_RIGHT, -vit)
        
        else :
            self.robot.set_motor_dps(MOTOR_LEFT, vit)
            self.robot.set_motor_dps(MOTOR_RIGHT, -vit)
        
        while(True):
            if(self.robot.get_motor_position[0] * self.robot.WHEEL_CIRCUMFERENCE):
                break
            if(self.robot.get_motor_position[1] * self.robot.WHEEL_CIRCUMFERENCE):
                break
