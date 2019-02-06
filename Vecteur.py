import numpy as np

class Vecteur():
    
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1    
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2
	
    def produitScalaire(self, v):
            return np.inner(self, v)
	
    def produitVectoriel(self,v):
        return np.cross(self, v)
        	
    def add(self, v):
        return Vecteur(self.x + v.x, self.y + v.y, self.z + v.z)
        
    def sub(self, v):
        return Vecteur(self.x - v.x, self.y - v.y, self.z - v.z)
