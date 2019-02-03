from Vecteur import*

class ObjetPhysique:

    def __init__(self, x, y, z, largeur = 5, longueur = 5, hauteur = 5, vecteur_direction = None):

        self.x = x
        self.y = y
        self.z = z
        self.largeur = largeur
        self.longueur = longueur
        self.hauteur = hauteur
        self.vecteur_direction = vecteur_direction # C'est bien un vecteur, non ?

        """
        Il faut en plus de définir des coordonnées, définir les dimensions l'objet (largeur x longueur x hauteur).
        Il sera plus de gérer des dimensions impaires.
        """


    
