#!/usr/bin/env python3
# -*- coding: utf-8 -*

from .objetphysique import ObjetPhysique
from math import radians,sqrt, cos, sin, pi
from .vecteur import Vecteur

class Robot(ObjetPhysique):

    WHEEL_BASE_WIDTH         = 117  # distance (mm) de la roue gauche a la roue droite.
    WHEEL_DIAMETER           = 66.5 #  diametre de la roue (mm)
    WHEEL_BASE_CIRCUMFERENCE = WHEEL_BASE_WIDTH * pi # perimetre du cercle de rotation (mm)
    WHEEL_CIRCUMFERENCE = WHEEL_DIAMETER * pi # perimetre de la roue (mm)

    def __init__(self, x, y, z, arene = None, id = 0): #dir, camera, rd, rg, detecteur, accelerometre):

        self.arene = arene
        
        ObjetPhysique.__init__(self, x, y, z, largeur = 100, longueur = 50, hauteur = 25)
        
        self.scalaire_rotation = 0
        self.scalaire_vitesse = 0
        
        self.MOTOR_LEFT = 0
        self.MOTOR_RIGHT = 0
        
        self.OFFSET_LEFT = 0
        self.OFFSET_RIGHT = 0
        
    def set_led(self, led, red = 0, green = 0,blue = 0):
        """ Allume une led. """
        pass
    
    def set_motor_dps(self,port,dps):
        """ Fixe la vitesse d'un moteur en nbr de degres par seconde
            :port: une constante moteur, MOTOR_LEFT ou MOTOR_RIGHT
            :dps: la vitesse cible en nombre de degres par seconde
        
        """
        if (port == MOTOR_LEFT):
            self.MOTOR_LEFT = dps
        elif (port == MOTOR_RIGHT):
            self.MOTOR_RIGHT = dps
        else :
            printf("ERREUR ROBOT_set_motor_dps : moteur invalide")
    
    
    def get_motor_position(self):
        """ Lit les etats des moteurs en degre.
        :return: couple du degre de rotation des moteurs
        
        """
        return (OFFSET_LEFT,OFFSET_RIGHT);
          
    def offset_motor_encoder(self, port, offset):
        """ Fixe l’offset des moteurs (en degres) (permet par exemple
        du moteur gauche avec offset_motor_encode(self.MOTOR_LEFT,self
        :port: un des deux moteurs MOTOR_LEFT ou MOTOR_RIGHT (ou les d
        :offset: l’offset de decalage en degre.
        Zero the encoder by offsetting it by the current position
        """
        if (port == MOTOR_LEFT):
            self.OFFSET_LEFT = offset;
        elif (port == MOTOR_RIGHT):
            self.OFFSET_RIGHT = offset;
        else :
            printf("ERREUR ROBOT_set_motor_dps : moteur invalide")
            
            
    def update_robot(self):
        """
        Met à jour la position et l'orientation du robot par rapport à scalaire_rotation,
        scalaire_vitesse, vecteur direction, SAUF S'IL Y A COLLISION
        
        """
        sauvx = self.x
        sauvy = self.y
        sauvdir = Vecteur(self.vecteur_direction.x,self.vecteur_direction.y,
                          self.vecteur_direction.z,)
    

        self.x += self.vecteur_direction.x * self.scalaire_vitesse
        self.y += self.vecteur_direction.y * self.scalaire_vitesse
        
        angle = radians(self.scalaire_rotation)
        cos_val = cos(angle)
        sin_val = sin(angle)

        
        self.vecteur_direction.x = self.vecteur_direction.x*cos_val -\
                                   self.vecteur_direction.y*sin_val
                                   
        self.vecteur_direction.y = self.vecteur_direction.x*sin_val +\
                                   self.vecteur_direction.y*cos_val
        
        
        if (self.arene.testCollision(self)): #Si on a des collisions
            self.x = sauvx
            self.y = sauvy
            self.vecteur_direction = sauvdir

        print(self.get_distance())
    
    def get_distance(self):
        """
        Mesure la distance entre le devant du robot et les objets devant.
        Retourne seulement l'objet dans la bonne direction et le plus proche du robot
        DETECTE LES AUTRES ROBOTS
        
        NE MARCHE QUE SI ROBOT A UNE ARENE !!!
        """
    
        if (self.arene == None):
            return
        
        obj = self.arene.objet + self.arene.robot
        
        def mmsigne(a,b): 
            if (a<0 and b<0):
                return True
            if (a==0 and b==0):
                return True
            return (a>0 and b>0)
            
        mini = 1000000
        p1 = (self.x,self.y)
        p2 = (self.x + (self.largeur /2)*self.vecteur_direction.x,
              self.y + (self.largeur /2)*self.vecteur_direction.y)
        
        if (round(p1[0]-p2[0],12) != 0): 
            a1 = (p1[1] - p2[1]) /(p1[0]- p2[0])
            b1 = p1[1] - a1*p1[0]
        else :
            a1 = None # Cas ou le robot est dans l'axe x
            b1 = p1[0]
            
        for o in obj:
            if (o == self):
                continue
                
            o = o.get_points()
            for j in range(len(o)):
                p3 = o[j]
                p4 = o[(j+1)%len(o)]#Marche avec un polygone à n cotées
                
                if (round(p3[0]-p4[0],12) !=0):
                    a2 = (p3[1] - p4[1])/(p3[0]- p4[0]) 
                    b2 = p3[1] - a2*p3[0]
                
                else :
                    a2 = None # Cas ou le segment est dans l'axe x
                    b2 = p4[0]
                
                if (a1 == a2) :
                    continue
                
                if (a1 == None) :
                    x = b1
                    y = a2*x + b2
                
                elif (a2 == None):
                    x = b2
                    y = a1*x + b1
                
                else :
                    x = (b2 - b1) / (a1 - a2)
                    y = a1*x + b1
                
                res = sqrt(pow(p2[0]-x,2)+pow(p2[1]-y,2))
                
                if mmsigne(p2[0] - p1[0],x - p1[0]) and mmsigne(p2[1] - p1[1],y - p1[1]):
                    
                    if (min(p3[0],p4[0])<=x<=max(p3[0],p4[0]) and 
                        min(p3[1],p4[1])<=y<=max(p3[1],p4[1])):
                        if (mini > res):
                            mini = res

        return mini
        

