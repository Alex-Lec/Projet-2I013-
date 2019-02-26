#!/usr/bin/env python3
# -*- coding: utf-8 -*

from composant import *
import pickle

class Terrain():

    def __init__(self, dimx = 1000, dimy = 600):
        
        self.dimx = dimx
        self.dimy = dimy
        self.objet = [ObjetPhysique(dimx/2, -1, 0, 0, dimx, 0),# haut
                      ObjetPhysique(-1, dimy/2, 0, dimy, 0, 0),# gauche
                      ObjetPhysique(dimx/2, dimy+1, 0, 0, dimx, 0),#bas
                      ObjetPhysique(dimx+1, dimy/2, 0, dimy, 0, 0)]#droite
        
        self.robot = []

    def avancer_robot(self, robot):
        robot.arene = self
        #robot.detecte(self.objet)
        robot.scalaire_vitesse = 10
        robot.update();
        robot.scalaire_vitesse = 0
            
    def reculer_robot(self, robot):
        robot.arene = self
        #robot.detecte(self.objet)
        robot.scalaire_vitesse = -10
        robot.update();
        robot.scalaire_vitesse = 0

    def tourner_robot_d(self, robot):
        robot.arene = self
        #robot.detecte(self.objet)
        robot.scalaire_rotation = 10
        robot.update();
        robot.scalaire_rotation =0
            
    def tourner_robot_g(self, robot):
        robot.arene = self
        #robot.detecte(self.objet)
        robot.scalaire_rotation = -10
        robot.update();
        robot.scalaire_rotation =0
            

    def testCollision(self, rob, obj):
    
        for i in range(len(rob.points)):
        
            p1 = rob.points[i]
            p2 = rob.points[(i+1)%len(rob.points)]
            
            if (p1[0]-p2[0] != 0): 
                a1 = (p1[1] - p2[1]) /(p1[0]- p2[0])
                b1 = p1[1] - a1*p1[0]
                
            else :
                a1 = None # Cas ou le robot est dans l'axe x
                b1 = p1[0]
                
            for o in obj:
                for j in range(len(o.points)):
                    p3 = o.points[j]
                    p4 = o.points[(j+1)%len(o.points)]#Marche avec un polygone à n cotées
                    
                    if (p3[0]-p4[0] !=0):
                        a2 = (p3[1] - p4[1])/(p3[0]- p4[0]) 
                        b2 = p3[1] - a2*p3[0]
                    
                    else :
                        a2 = None # Cas ou le segment est dans l'axe x
                        b2 = p4[0]
                    
                    if (a1 == a2) :
                        continue
                    
                    if (a1 == None) :
                        x = b1
                        y = a2*x + b2
                    
                    elif (a2 == None):
                        x = b2
                        y = a1*x + b1
                    
                    else :
                        x = (b2 - b1) / (a1 - a2)
                        y = a1*x + b1
                     
                    if (min(p3[0],p4[0])<=x<=max(p3[0],p4[0]) and 
                        min(p3[1],p4[1])<=y<=max(p3[1],p4[1]) and 
                        min(p1[0],p2[0])<=x<=max(p1[0],p2[0]) and 
                        min(p1[1],p2[1])<=y<=max(p1[1],p2[1])):
                        
                        return False
        return True
        
    def sauvegarder_arene(self, fichier):

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
