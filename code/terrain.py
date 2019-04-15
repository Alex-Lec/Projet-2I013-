#!/usr/bin/env python3
# -*- coding: utf-8 -*

from composant import *
import pickle
from math import radians,sqrt, cos, sin, pi
from threading import Thread
import time 

class Terrain(Thread):

    def __init__(self, dimx = 1500, dimy = 900):
        super(Terrain,self).__init__()
        self.dimx = dimx
        self.dimy = dimy
        self.objet = [ObjetPhysique(dimx/2, -1, 0, 1, dimx, 100),# haut
                      ObjetPhysique(-1, dimy/2, 0, dimy, 1, 100),# gauche
                      ObjetPhysique(dimx/2, dimy+1, 0, 1, dimx, 100),#bas
                      ObjetPhysique(dimx+1, dimy/2, 0, dimy, 1, 100)]#droite

        self.zones_grises = []
        
        self.robot = []
        self.tps = 30
        self.last_up = time.time()
        
    def run(self):
        while True :
            self.update()
            time.sleep(1./self.tps)

    def avancer_robot(self, robot):
        robot.arene = self
        robot.MOTOR_LEFT = 15
        robot.MOTOR_RIGHT = 15
        robot.last_up = time.time()-1
        self.update()
            
    def reculer_robot(self, robot):
        robot.arene = self
        robot.MOTOR_LEFT = -15
        robot.MOTOR_RIGHT = -15
        robot.last_up = time.time()-1
        self.update()

    def tourner_robot_d(self, robot):
        robot.arene = self
        robot.MOTOR_LEFT = 15
        robot.MOTOR_RIGHT = 0
        robot.last_up = time.time()-1
        self.update()
            
    def tourner_robot_g(self, robot):
        robot.arene = self
        robot.MOTOR_LEFT = 0
        robot.MOTOR_RIGHT = 15
        robot.last_up = time.time()-1
        self.update()

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
                if (o == rob or o == projection ):
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
                        
                        #On vérifie à présent si les objets sont à la même hauteur
                        brob = min(rob.z, rob.z + rob.hauteur)
                        hrob = max(rob.z, rob.z + rob.hauteur)
                        
                        bobj = min(o.z, o.z + o.hauteur)
                        hobj = max(o.z, o.z + o.hauteur)
                        if (brob <= hobj and bobj <= hrob):
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
