class Vecteur():
	def __init__(self, x, y, z):
	    self.x = x
	    self.y = y
	    self.z = z
    
    def produitScalaire(self, v):
        return Vecteur(x + v.x, y + v.y, z + v.z)
