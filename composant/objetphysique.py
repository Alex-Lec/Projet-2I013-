from .vecteur import Vecteur
class ObjetPhysique:

    def __init__(self, x = 0, y = 0, z = 0, longueur = 50, largeur = 100, hauteur = 20):
       
        self.x = x
        self.y = y
        self.z = z
        self.largeur = largeur
        self.longueur = longueur
        self.hauteur = hauteur
        self.vecteur_direction = Vecteur(1., 0., 0.)

        self.points = [
            (x + self.largeur // 2, y + self.longueur // 2),
            (x + self.largeur // 2, y - self.longueur // 2),
            (x - self.largeur // 2, y - self.longueur // 2),
            (x - self.largeur // 2, y + self.longueur // 2)
        ]

