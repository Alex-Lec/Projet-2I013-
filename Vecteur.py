import numpy as np

class Vecteur():
    """
    Classe Vecteur :
    x, y ,z);
    """
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2
	
    def produitScalaire(self, s):
            self.x1 *= s
            self.y1 *= s
            self.z1 *= s
            self.x2 *= s
            self.y2 *= s
            self.z2 *= s
	
    def produitVectoriel(self, v):
        return np.cross(self, v)

    def add(self, v):
        return Vecteur(self.x + v.x, self.y + v.y, self.z + v.z)

    def sub(self, v):
        return Vecteur(self.x - v.x, self.y - v.y, self.z - v.z)
