#!/usr/bin/env python3
# -*- coding: utf-8 -*

from composant import *
import pickle
from math import radians,sqrt, cos, sin, pi

class Terrain():

    def __init__(self, dimx = 1000, dimy = 600):
        
        self.dimx = dimx
        self.dimy = dimy
        self.objet = [ObjetPhysique(dimx/2, -1, 0, 1, dimx, 0),# haut
                      ObjetPhysique(-1, dimy/2, 0, dimy, 1, 0),# gauche
                      ObjetPhysique(dimx/2, dimy+1, 0, 1, dimx, 0),#bas
                      ObjetPhysique(dimx+1, dimy/2, 0, dimy, 1, 0)]#droite
        
        self.robot = []

    def avancer_robot(self, robot):
        robot.arene = self
        #robot.detecte(self.objet)
        robot.scalaire_vitesse = 10
        self.update();
        robot.scalaire_vitesse = 0
            
    def reculer_robot(self, robot):
        robot.arene = self
        #robot.detecte(self.objet)
        robot.scalaire_vitesse = -10
        self.update();
        robot.scalaire_vitesse = 0

    def tourner_robot_d(self, robot):
        robot.arene = self
        #robot.detecte(self.objet)
        robot.scalaire_rotation = 10
        self.update();
        robot.scalaire_rotation =0
            
    def tourner_robot_g(self, robot):
        robot.arene = self
        #robot.detecte(self.objet)
        robot.scalaire_rotation = -10
        self.update();
        robot.scalaire_rotation =0
        

    def update(self):
        self.update_robot()

    def update_robot(self):
        """
        Met à jour la position et l'orientation du robot par rapport à scalaire_rotation,
        scalaire_vitesse, vecteur direction, SAUF S'IL Y A COLLISION
        
        """
        for rob in self.robot:
            sauvx = rob.x
            sauvy = rob.y
            sauvdir = Vecteur(rob.vecteur_direction.x,rob.vecteur_direction.y,
                              rob.vecteur_direction.z,)
        
            vx = rob.vecteur_direction.x * rob.scalaire_vitesse
            vy = rob.vecteur_direction.y * rob.scalaire_vitesse
            
            rob.x += vx
            rob.y += vy
            
            for i in range(len(rob.points)):
                j = rob.points[i]
                
                rob.points[i]= (j[0] + vx, j[1] + vy)
            
            angle = radians(rob.scalaire_rotation)
            cos_val = cos(angle)
            sin_val = sin(angle)
            
            x1 = rob.vecteur_direction.x
            y1 = rob.vecteur_direction.y
            
            rob.vecteur_direction.x = x1*cos_val - y1*sin_val
            rob.vecteur_direction.y = x1*sin_val + y1*cos_val
            
            rob.points = rob.get_points()
            
            if (self.testCollision(rob)): #Si on a des collisions
                rob.x = sauvx
                rob.y = sauvy
                rob.vecteur_direction = sauvdir
                rob.points = rob.get_points()

            
            print(rob.get_distance())
        
        

    def testCollision(self, rob):
        
        obj = self.objet + self.robot
        
        robpts = rob.get_points()
        for i in range(len(robpts)):
        
            p1 = robpts[i]
            p2 = robpts[(i+1)%len(robpts)]
            
            if (round(p1[0]-p2[0],12) != 0): 
                a1 = (p1[1] - p2[1]) /(p1[0]- p2[0])
                b1 = p1[1] - a1*p1[0]
                
            else :
                a1 = None # Cas ou le robot est dans l'axe x
                b1 = p1[0]
                
            for o in obj:
                if (o == rob):
                    continue
                opts = o.get_points()
                for j in range(len(opts)):
                    p3 = opts[j]
                    p4 = opts[(j+1)%len(opts)]#Marche avec un polygone à n cotées
                    
                    if (round(p3[0]-p4[0],12) !=0):
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
                        
                        return True
                    
        return False
        
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
