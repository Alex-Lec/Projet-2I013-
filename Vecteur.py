import numpy as np

class Vecteur():
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	
	def produitScalaire(self, v):
        	return np.inner(self, v)
	
	def produitVectoriel(self,v):
		return np.cross(self, v)
	
	def add(self, v):
		return Vecteur(self.x + v.x, self.y + v.y, self.z + v.z)
	
	def sub(self, v):
		return Vecteur(self.x - v.x, self.y - v.y, self.z - v.z)
