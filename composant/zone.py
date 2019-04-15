from .objetphysique import ObjetPhysique

class Zone(ObjetPhysique):
    def __init__(self, x, y, largeur, longueur): 
        ObjetPhysique.__init__(self, x, y, 0, largeur, longueur, 0)
        
