#!/usr/bin/env python3
# -*- coding: utf-8 -*

import time
from diver import *
from controleur import Controleur_carre, Controleur_droit_stop, Controleur_image, Controleur_tour, Controleur_polygone
import sys
from PIL import Image
import os 

class Simulation():
    def __init__(self, robot = None, arene = None):
        self.robot = robot
        self.affichage = None
        self.arene = arene
        self.controleur = None
        self.choix_controleur(self.menu())
    
    def menu(self):
        os.system("clear")
        print("\n\
                       Bienvenue dans la matrice\n\
                       Selectionnez votre choix\n\n\
                    #  Controleur_carre           -> 1 #\n\
                    #  Controleur_droit_stop      -> 2 #\n\
                    #  Controleur_tour            -> 3 #\n\
                    #  Controleur_polygone        -> 4 #\n\
                    #  Controleur_image           -> 5 #\n\n\
                    #  Charger une arene          -> C #\n\
                    #  Quit                       -> Q #")

        return input()


    def menu_affichage(self):
        if (self.robot != None):
            return "O"
            
        print("\n\
                             Controleur 2D ou 3D :      \n\n\
                    #              2D   -> 1           #\n\
                    #              3D   -> 2           #\n")
                    
        return input()

    def dimension(self,dim):
        if (dim == "1"):
            self.robot = Robot(x = 100, y = 100, z = 0, arene = self.arene)
            self.arene.robot.append(self.robot)
            self.affichage = Affichage(self.arene)
            
        elif (dim == "2"):
            self.robot = Robot(x = 100, y = 100, z = 0,\
                         largeur = 10, longueur = 10, hauteur = 10, arene = self.arene)
            self.arene.robot.append(self.robot)
            self.affichage = Affichage_3D(arene = self.arene, width = 1000, height = 600,\
                                     caption = 'Robot 2I013')

    def choix_controleur(self,choix):
        if (choix == "1"):
            self.dimension(self.menu_affichage())
            self.controleur = Controleur_carre(self.robot,500,500)

        elif (choix == "2"):
            self.dimension(self.menu_affichage())
            self.controleur = Controleur_droit_stop(self.robot, dst = 100)
            
        elif (choix == "3"):
            self.dimension(self.menu_affichage())
            self.controleur = Controleur_tour(self.robot)
            
        elif (choix == "4"):
            self.dimension(self.menu_affichage())
            print("\n\
                        Nombre de côté :")
            cote = input()
            self.controleur = Controleur_polygone(self.robot, int(cote))
            
        elif (choix == "5"):
            self.dimension(self.menu_affichage())
            self.controleur = Controleur_image(self.robot)
            
        elif (choix == "c" or choix == "C"):
            if (self.arene != None):
                print("Nom de fichier à charger :")
                nom_fichier = input()
                self.arene.objet[4:] = []
                self.arene.ouvrir_arene("arenes/"+nom_fichier)
            
            self.choix_controleur(self.menu())
        
        else :
            sys.exit()



###################################################################
###################################################################
###################################################################

simu = None

try:
    from robot2I013.robot2I013 import Robot2I013
    simu = Simulation(Robot2I013())
    
except(ImportError):
    from composant import Robot, Rectangle
    from code import Affichage, Affichage_3D, Terrain
    arene = Terrain()
    arene.objet.append(Rectangle(25, 100, 0, 100, 50, 20))
    arene.objet.append(Rectangle(500, 300, 50, 100, 100, 10))
    #arene.objet.append(Rectangle(745, 145, 0, 10, 10, 99))
    
    simu = Simulation(None,arene)
    
if (simu.affichage != None):
    simu.affichage.start()

if (simu.arene != None):
    simu.arene.start()
    
tps = 100
simu.controleur.start()
while simu.controleur.stop():
    simu.controleur.step()
    time.sleep(1/tps)
print("stop")
sys.exit()
