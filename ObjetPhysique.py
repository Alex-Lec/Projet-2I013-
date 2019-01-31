class ObjetPhysique:

    def __init__(self, x, y, z, cote, dir):
        self.x = x
        self.y = y
        self.z = z
        self.cote = cote
        self.dir = dir
    
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
    
    def get_cote(self):
        return self.cote
    
    def get_dir(self):
        return self.dir
    
    def set_dir(self, ndir):
        self.dir = ndir
