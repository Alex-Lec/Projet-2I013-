class ObjetPhysique:

    def __init__(self, x = 0, y = 0, z = 0, longueur = 50, largeur = 100, hauteur = 20):
        self.x = x
        self.y = y
        self.z = z
        self.largeur = largeur
        self.longueur = longueur
        self.hauteur = hauteur

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_z(self, z):
        self.z = z

    def get_dim(self):
        return (self.longueur, self.largeur, self.hauteur)

    def get_dir(self):
        return self.dir

    def set_dir(self, ndir):
        self.dir = ndir
