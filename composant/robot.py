#!/usr/bin/env python3
# -*- coding: utf-8 -*

from .objetphysique import ObjetPhysique
from .detecteur import Detecteur
from math import radians,sqrt, cos, sin, pi
from .vecteur import Vecteur
import time

class Robot(ObjetPhysique):

    WHEEL_BASE_WIDTH         = 117  # distance (mm) de la roue gauche a la roue droite.
    WHEEL_DIAMETER           = 66.5 #  diametre de la roue (mm)
    WHEEL_BASE_CIRCUMFERENCE = WHEEL_BASE_WIDTH * pi # perimetre du cercle de rotation (mm)
    WHEEL_CIRCUMFERENCE = WHEEL_DIAMETER * pi # perimetre de la roue (mm)

    def __init__(self, x, y, z, arene = None, id = 0): 
        self.arene = arene
        ObjetPhysique.__init__(self, x, y, z, largeur = 50, longueur = 100, hauteur = 25)
        
        self.detecteur = Detecteur(self)
        self.MOTOR_LEFT = 1
        self.MOTOR_RIGHT = 2
        
        self.OFFSET_LEFT = 0
        self.OFFSET_RIGHT = 0
        
        
        self.last_up = time.time()
        
    def set_led(self, led, red = 0, green = 0,blue = 0):
        """ Allume une led. """
        pass
    
    def set_motor_dps(self,port ,dps):
        """ Fixe la vitesse d'un moteur en nbr de degres par seconde
            :port: une constante moteur, MOTOR_LEFT ou MOTOR_RIGHT
            :dps: la vitesse cible en nombre de degres par seconde
        
        """
        if (port == 1):
            self.MOTOR_LEFT = dps
        elif (port == 2):
            self.MOTOR_RIGHT = dps
        else :
            print("ERREUR ROBOT_set_motor_dps : moteur invalide")
    
    
    def get_motor_position(self):
        """ Lit les etats des moteurs en degre.
        :return: couple du degre de rotation des moteurs
        
        """
        return (self.OFFSET_LEFT,self.OFFSET_RIGHT);
          
    def offset_motor_encoder(self, port, offset):
        """ Fixe l’offset des moteurs (en degres) (permet par exemple
        du moteur gauche avec offset_motor_encode(self.MOTOR_LEFT,self
        :port: un des deux moteurs MOTOR_LEFT ou MOTOR_RIGHT (ou les d
        :offset: l’offset de decalage en degre.
        Zero the encoder by offsetting it by the current position
        """
        if (port == 3):
            self.OFFSET_LEFT  -= offset;
            self.OFFSET_RIGHT -= offset;
        elif (port == 1):
            self.OFFSET_LEFT  -= offset;
        elif (port == 2):
            self.OFFSET_RIGHT -= offset;
        else :
            print("ERREUR ROBOT_motor_encoder : moteur invalide")  
            
    def update_robot(self):
        """
        N'APPARTIENT PAS A LA CLASSE ROBOT PHYSIQUE NE PAS L'UTILISER DANS LES STRATEGIES 
        Met à jour la position et l'orientation du robot par rapport à v_rotation,
        vitesse, vecteur direction, SAUF S'IL Y A COLLISION
        
        """
        ################################################################
        x = self.x
        y = self.y
        v_x = self.v_dir.x
        v_y = self.v_dir.y
        
        rot = 25
        t = time.time()
        ################################
        for i in range(rot):
            omega1 = ((self.MOTOR_LEFT *(t - self.last_up)/rot)*self.WHEEL_CIRCUMFERENCE) /(2*self.WHEEL_BASE_CIRCUMFERENCE)
            omega2 = ((self.MOTOR_RIGHT*(t - self.last_up)/rot)*self.WHEEL_CIRCUMFERENCE) /(2*self.WHEEL_BASE_CIRCUMFERENCE)
            
            cos_val = cos(-radians(omega2))
            sin_val = sin(-radians(omega2))
            xo =  x + v_y * (self.WHEEL_BASE_WIDTH/2)
            yo =  y - v_x * (self.WHEEL_BASE_WIDTH/2)
            x = (x-xo)*cos_val - (y-yo)*sin_val + xo
            y = (x-xo)*sin_val + (y-yo)*cos_val + yo
            v_x = v_x*cos_val - v_y*sin_val
            v_y = v_x*sin_val + v_y*cos_val
            
            cos_val = cos(radians(omega1))
            sin_val = sin(radians(omega1))
            xo = x - v_y * (self.WHEEL_BASE_WIDTH/2) 
            yo = y + v_x * (self.WHEEL_BASE_WIDTH/2)
            x = (x-xo)*cos_val - (y-yo)*sin_val + xo
            y = (x-xo)*sin_val + (y-yo)*cos_val + yo
            v_x = v_x*cos_val - v_y*sin_val
            v_y = v_x*sin_val + v_y*cos_val
            
        ##############################################################        
        #print(self.v_dir.x , self.v_dir.y)
        v_d = Vecteur(v_x,v_y,self.v_dir.z)
        
        robTest = Robot(x,y,0)
        robTest.v_dir = v_d

        self.OFFSET_LEFT  += self.MOTOR_LEFT*(t - self.last_up)
        self.OFFSET_RIGHT += self.MOTOR_RIGHT*(t - self.last_up)

        #print(self.get_distance())
        self.last_up = time.time()
        
        if (self.arene.testCollision(robTest,self) == False):
            self.x = x
            self.y = y
            self.v_dir = v_d
        
        
    def get_distance(self):
        """
        Mesure la distance entre le devant du robot et les objets devant.
        Retourne seulement l'objet dans la bonne direction et le plus proche du robot
        DETECTE LES AUTRES ROBOTS
        
        NE MARCHE QUE SI ROBOT A UNE ARENE !!!
        """
        return self.detecteur.detecte()


