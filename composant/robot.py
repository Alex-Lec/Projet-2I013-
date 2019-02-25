#!/usr/bin/env python3
# -*- coding: utf-8 -*

from .objetphysique import ObjetPhysique
from .vecteur import Vecteur


import math
class Robot(ObjetPhysique):

    def __init__(self, x, y, z): #dir, camera, rd, rg, detecteur, accelerometre):

        ObjetPhysique.__init__(self, x, y, z, largeur = 100, longueur = 50, hauteur = 25)
        self.event = []
        self.vecteur_direction = Vecteur(1., 0., 0.)
        self.scalaire_rotation = 2
        self.scalaire_vitesse = 0
        
        self.vitesse_moteur_g = 0
        self.vitesse_moteur_d = 0
        
        self.rayon_roue_g = 
        self.rayon_roue_d = 
        
    def set_led(self, led, red = 0, green = 0,blue = 0):
        """ Allume une led. """
        pass
    
    
    def set_motor_dps(self,port,dps):
        """ Fixe la vitesse d'un moteur en nbr de degres par seconde
            :port: une constante moteur, MOTOR_LEFT ou MOTOR_RIGHT
            :dps: la vitesse cible en nombre de degres par seconde
        
        """
        pass
    
    
    def get_motor_position(self):
        """ Lit les etats des moteurs en degre.
        :return: couple du degre de rotation des moteurs
        
        """
        pass
        
        
    def offset_motor_encoder(self, port, offset):
        """ Fixe l’offset des moteurs (en degres) (permet par exemple
        du moteur gauche avec offset_motor_encode(self.MOTOR_LEFT,self
        :port: un des deux moteurs MOTOR_LEFT ou MOTOR_RIGHT (ou les d
        :offset: l’offset de decalage en degre.
        Zero the encoder by offsetting it by the current position
        """
        pass
        
    
        
    def update(self):
        
    
        vx = self.vecteur_direction.x * self.scalaire_vitesse
        vy = self.vecteur_direction.y * self.scalaire_vitesse
        
        self.x += vx
        self.y += vy
        
        for i in range(len(self.points)):
            j = self.points[i]
            
            self.points[i]= (j[0] + vx, j[1] + vy)
        
        angle = math.radians(self.scalaire_rotation)
        cos_val = math.cos(angle)
        sin_val = math.sin(angle)
        
        x1 = self.vecteur_direction.x
        y1 = self.vecteur_direction.y
        
        self.vecteur_direction.x = x1*cos_val - y1*sin_val
        self.vecteur_direction.y = x1*sin_val + y1*cos_val
        
        for i in range(len(self.points)):
            j = self.points[i]
            x_new = (j[0] - self.x) * cos_val - (j[1] - self.y) * sin_val
            y_new = (j[0] - self.x) * sin_val + (j[1] - self.y) * cos_val
            
            self.points[i]= (x_new + self.x, y_new + self.y)
            
    
    
    def get_distance(self,obj=[]):
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
        
        if (p1[0]-p2[0] != 0): 
            a1 = (p1[1] - p2[1]) /(p1[0]- p2[0])
            b1 = p1[1] - a1*p1[0]
        else :
            a1 = None # Cas ou le robot est dans l'axe x
            b1 = p1[0]
            
        for o in obj:
            for j in range(len(o.points)):
                p3 = o.points[j]
                p4 = o.points[(j+1)%len(o.points)]#Marche avec un polygone à n cotées
                
                if (p3[0]-p4[0] !=0):
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
        
