class ObjetPhysique:

    def __init__(self, x, y, z, dir):
        self.x = x
        self.y = y
        self.z = z
        self.dir = dir
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_z(self):
        return self.z
    
    def get_dir(self):
        return self.dir
    
    def set_dir(self, ndir):
        self.dir = ndir
