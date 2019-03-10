from composant import Robot, ObjetPhysique
import time
from math import pi

class Strategie:
    def __init__(self, robot):
        self.robot = robot
        self.stop = False
    
    def avancer(self,dst, vit):
        if (self.stop == True) :
            return
        self.robot.set_motor_dps("MOTOR_LEFT" , vit)
        self.robot.set_motor_dps("MOTOR_RIGHT", vit)
        self.robot.offset_motor_encoder("MOTOR_LEFT_RIGHT", 0)
        
        while(self.stop != True):
            
            if((self.robot.get_motor_position()[0]*self.robot.WHEEL_CIRCUMFERENCE)
                /360 > dst):
                self.robot.set_motor_dps("MOTOR_LEFT" , 0)
                self.robot.set_motor_dps("MOTOR_RIGHT", 0)
                self.stop = True
                return
            if((self.robot.get_motor_position()[1]*self.robot.WHEEL_CIRCUMFERENCE)
                /360 > dst):
                self.robot.set_motor_dps("MOTOR_LEFT" , 0)
                self.robot.set_motor_dps("MOTOR_RIGHT", 0)
                self.stop = True
                return
    
    def reculer(self,dst, vit):
        if (self.stop == True) :
            return
        self.robot.set_motor_dps("MOTOR_LEFT" , -vit)
        self.robot.set_motor_dps("MOTOR_RIGHT", -vit)
        self.robot.offset_motor_encoder("MOTOR_LEFT_RIGHT", 0)
        
        while(self.stop != True):
            
            if((self.robot.get_motor_position()[0]*self.robot.WHEEL_CIRCUMFERENCE)
                /360 < -dst):
                self.robot.set_motor_dps("MOTOR_LEFT" , 0)
                self.robot.set_motor_dps("MOTOR_RIGHT", 0)
                self.stop = True
                return
            if((self.robot.get_motor_position()[1]*self.robot.WHEEL_CIRCUMFERENCE)
                /360 < -dst):
                self.robot.set_motor_dps("MOTOR_LEFT" , 0)
                self.robot.set_motor_dps("MOTOR_RIGHT", 0)
                self.stop = True
                return
    
    def tourner(self,angle, vit):
        if (self.stop == True) :
            return
        self.robot.set_motor_dps("MOTOR_LEFT" ,  vit)
        self.robot.set_motor_dps("MOTOR_RIGHT", -vit)
        self.robot.offset_motor_encoder("MOTOR_LEFT_RIGHT", 0)
        
        while(self.stop != True):
            if((self.robot.get_motor_position()[0]*360/self.robot.WHEEL_BASE_CIRCUMFERENCE) 
                > angle):
                self.robot.set_motor_dps("MOTOR_LEFT" , 0)
                self.robot.set_motor_dps("MOTOR_RIGHT", 0)
                self.stop = True
                print("stop 1")
                return
            
            if((self.robot.get_motor_position()[1]*360 /self.robot.WHEEL_BASE_CIRCUMFERENCE)
                < -angle):
                
                self.robot.set_motor_dps("MOTOR_LEFT" , 0)
                self.robot.set_motor_dps("MOTOR_RIGHT", 0)
                self.stop = True
                print("stop 2")
                return
