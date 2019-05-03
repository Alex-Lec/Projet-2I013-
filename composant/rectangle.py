from .objetphysique import ObjetPhysique
import numpy as np
from math import radians,sqrt, cos, sin, pi

class Rectangle(ObjetPhysique):
    
    def get_points(self):
    
        # Vecteur vers devant le robot
        v_x = self.v_dir.x*(self.longueur//2) 
        v_y = self.v_dir.y*(self.longueur//2)
        
        # Vecteur vers la gauche du robot
        v_xg = -self.v_dir.y*(self.largeur//2)
        v_yg =  self.v_dir.x*(self.largeur//2)
        
        # Vecteur vers la droite du robot
        v_xd =  self.v_dir.y*(self.largeur//2)
        v_yd = -self.v_dir.x*(self.largeur//2)
        
        # Vecteur vers derrière le robot
        v_xb = -self.v_dir.x*(self.longueur//2)
        v_yb = -self.v_dir.y*(self.longueur//2)
    
        # Premier point devant à gauche du robot, deuxiéme devant à droite du robot,...
        pts=[[self.x + v_x  + v_xg, self.y + v_y  + v_yg],\
             [self.x + v_x  + v_xd, self.y + v_y  + v_yd],\
             [self.x + v_xb + v_xd, self.y + v_yb + v_yd],\
             [self.x + v_xb + v_xg, self.y + v_yb + v_yg]]
        
        return pts


