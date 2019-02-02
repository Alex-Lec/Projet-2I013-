import ObjetPhysique from *

class Terrain():

    def __init__(self, dimx, dimy):
        self.dimx = dimx;
        self.dimy = dimy;
        self.objet = []

    def ajouter_robot(self, x,y):
        c = Camera()
        rg = Roue()
        rd = Roue()
        d = Detecteur()
        a = Accelerometre()
        dir = Vecteur(0.0, 0.0, 0.0)
        r = Robot(x, y, dir, c, rd, rg, d, a)
        self.objet.append(r)

    def ajouter_objet(self, o):
        self.objet.append(o)

    def afficher_terrain():
        pass
    
    def testCollision(self, i1, i2):
        o1 = self.objet[i1]
        o2 = self.objet[i2]
        ovx = min(o1.get_x() + o1.get_cote(), o2.get_x() + o2.get_cote()) - max(o1.get_x() - o1.get_cote(), o2.get_x() - o2.get_cote()) > 0
        ovy = min(o1.get_y() + o1.get_cote(), o2.get_y() + o2.get_cote()) - max(o1.get_y() - o1.get_cote(), o2.get_y() - o2.get_cote()) > 0
        return ovx & ovy
    
    def checkCollisions (self):
        for i in range(len(self.objet)):
            try:
                for j in range(len(self.objet)):
                    if i == j:
                        continue
                    if testCollision(i, j):
                        raise ValueError()
            except ValueError:
                o1 = self.objet[i]
                o2 = self.objet[j]
                if o1.get_x() + o1.get_cote() < o2.get_x() - o2.get_cote():
                    o2.set_x(o2.get_x() + (o2.get_x() - o2.get_cote() - o1.get_x() - o1.get_cote()) + 1)
                else:
                    o2.set_x(o2.get_x() - (o1.get_x() + o1.get_cote() - o2.get_x() + o2.get_cote()) - 1)
                if o1.get_y() + o1.get_cote() < o2.get_y() - o2.get_cote():
                    o2.set_y(o2.get_y() + (o2.get_y() - o2.get_cote() - o1.get_y() - o1.get_cote()) + 1)
                o1.set_dir(Vecteur(0.0,0.0,0.0).sub(o1.get_dir()))  
                o2.set_dir(Vecteur(0.0,0.0,0.0).sub(o2.get_dir()))
            
