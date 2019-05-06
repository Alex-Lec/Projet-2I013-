#!/usr/bin/env python3
# -*- coding: utf-8 -*

from composant import Rectangle, Robot
import pickle
from math import radians,sqrt, cos, sin, pi
from threading import Thread
import time 

class Terrain(Thread):

    def __init__(self, dimx = 1500, dimy = 900):
        super(Terrain,self).__init__()
        self.dimx = dimx
        self.dimy = dimy
        
        # Bords de l'arène
        self.objet = [Rectangle(dimx/2, -1, 0, 1, dimx, 100),# Mur haut
                      Rectangle(-1, dimy/2, 0, dimy, 1, 100),# Mur gauche
                      Rectangle(dimx/2, dimy+1, 0, 1, dimx, 100),# Mur bas
                      Rectangle(dimx+1, dimy/2, 0, dimy, 1, 100)]# Mur droite
        
        self.robot = [] # Liste des robots contenus dans l'arène
        self.tps = 30   # Temps de refraichissement de l'arène
        
    def run(self):
        while True :
            self.update()
            time.sleep(1./self.tps)

    def update(self):
        for rob in self.robot:
            rob.arene = self
            rob.update_robot()

    def testCollision(self, rob, projection = None):
        """
        Detecte lorsque deux segments d'objets se rencontre.
        Renvoie true s'il y a collision, false sinon.
        Projection sert à tester la position suivante du robot.
        """
        
        obj = self.objet + self.robot
        
        robpts = rob.get_points()
        for i in range(len(robpts)): # On iter sur les points du robots
            #On transforme chaques pts en segment avec le pts suivant dans la liste
            
            p1 = robpts[i]
            p2 = robpts[(i+1)%len(robpts)]
            
            # Si le segment n'est pas vertical
            # On crée la droite passant par le segment
            if (round(p1[0]-p2[0],12) != 0): 
                a1 = (p1[1] - p2[1]) /(p1[0]- p2[0])
                b1 = p1[1] - a1*p1[0]
                
            # Si le segment est dans l'axe x
            # On note l'information dans a1
            else :
                a1 = None
                b1 = p1[0]
                
            for o in obj:
                if (o == rob or o == projection ):
                    continue
                    
                    
                opts = o.get_points()
                for j in range(len(opts)):# On iter sur les points du robots
                    #On transforme chaques pts en segment avec le pts suivant dans la liste
                    p3 = opts[j]
                    p4 = opts[(j+1)%len(opts)]#Marche avec un polygone à n cotées
                    
                    
                    # Si le segment n'est pas vertical
                    # On crée la droite passant par le segment
                    if (round(p3[0]-p4[0],12) !=0):
                        a2 = (p3[1] - p4[1])/(p3[0]- p4[0]) 
                        b2 = p3[1] - a2*p3[0]
                    
                    # Si le segment est dans l'axe x
                    # On note l'information dans a2
                    else :
                        a2 = None
                        b2 = p4[0]
                    
                    if (a1 == a2) :# Les droites sont parallèles, pas d'intersection, fin
                        continue
                    
                    # On trouve le pts d'intersection des droites
                    if (a1 == None) :
                        x = b1
                        y = a2*x + b2
                    elif (a2 == None):
                        x = b2
                        y = a1*x + b1
                    else :
                        x = (b2 - b1) / (a1 - a2)
                        y = a1*x + b1
                     
                    # On vérifie que le point d'interswection des droites ce trouve sur le
                    # segment de l'objet ET le segment du robot
                    if (min(p3[0],p4[0])<=x<=max(p3[0],p4[0]) and 
                        min(p3[1],p4[1])<=y<=max(p3[1],p4[1]) and 
                        min(p1[0],p2[0])<=x<=max(p1[0],p2[0]) and 
                        min(p1[1],p2[1])<=y<=max(p1[1],p2[1])):
                        
                        #On vérifie à présent si les objets sont à la même hauteur
                        brob = min(rob.z, rob.z + rob.hauteur)
                        hrob = max(rob.z, rob.z + rob.hauteur)
                        
                        bobj = min(o.z, o.z + o.hauteur)
                        hobj = max(o.z, o.z + o.hauteur)
                        if (brob <= hobj and bobj <= hrob):
                            return True
                    
        return False
        
    def sauvegarder_arene(self, fichier):

        """
        Sauvegarde une arène dans un fichier à l'aide de Pickle
        """

        try :
            with open(fichier, 'wb') as fichier:
                arene = pickle.Pickler(fichier)
                arene.dump(self.dimx)
                arene.dump(self.dimy)
                arene.dump(self.objet)
                arene.dump(self.robot)
                
        except IOError:
            print("Le fichier n'a pas pu être ouvert !")
            pass

    def ouvrir_arene(self, fichier):

        """
        Charge une arène à partir d'un fichier à l'aide de Pickle
        """

        try:
            with open(fichier, 'rb') as fichier:
                arene_pickle = pickle.Unpickler(fichier)
                self.dimx = arene_pickle.load() 
                self.dimy = arene_pickle.load() 
                self.objet = arene_pickle.load() 
                self.robot = arene_pickle.load()

        except FileNotFoundError:
            print("Le fichier n'existe pas !")
            pass
