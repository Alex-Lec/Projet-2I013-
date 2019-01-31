# -*-coding:utf-8 -*

class Robot(ObjetPhysique):
    """
    Classe Robot :
    position (x, y);
    Camera;
    Roue droite, gauche;
    Detecteur;
    Acceleremetre.
    """

    def __init__(self, x, y, z, dir, camera, rd, rg, detecteur, accelerometre):
        ObjetPhysique(x, y, z, dir)
        self.camera = camera
        self.rd = rd
        self.rg = rg
        self.detecteur = detecteur
        self.accelerometre = accelerometre

    def avancer(self, distance):
        pass

    def reculer(self, distance):
        pass

    def tourner(self, angle):
        pass
