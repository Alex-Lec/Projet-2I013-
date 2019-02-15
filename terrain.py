#!/usr/bin/env python3
# -*- coding: utf-8 -*

from composant import *
#from Vecteur import *
#from Camera import *
#from Roue import *
#from Detecteur import *
#from Accelerometre import *
#from Robot import *
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
        
    """ 
        def ajouter_robot(self, x, y, z):
            c = Camera()
            rg = Roue()
            rd = Roue()
            d = Detecteur()
            a = Accelerometre()
            vdir = Vecteur(20, 0.0, 0.0)
            r = Robot(x, y, dir,)
            self.objet.append(r)
    """

    def avancer_robot(self, robot):
        #print(self.testCollision(robot,self.objet))
        robot.detecte(self.objet)
        if (self.testCollision(robot,self.objet)):
            robot.avancer()

    def tourner_robot(self, robot):
        #print(self.testCollision(robot,self.objet))
        robot.detecte(self.objet)
        if (self.testCollision(robot,self.objet)):
            robot.tourner()

    def ajouter_objets(self, o): #prend une liste d'object en arguement
        for i in o:
            self.objet.append(i)
            
    def ajouter_robots(self,o):
        for i in o:
            self.robot.append(i)
    
    def testCollision(self, rob, obj):

        for i in range(len(rob.points)) :
        
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
                if o1.get_x() + o1.get_dim()[0] < o2.get_x() - o2.get_dim()[0]:
                    o2.set_x(o2.get_x() + (o2.get_x() - o2.get_dim()[0] - o1.get_x() - o1.get_dim()[0]) + 1)
                else:
                    o2.set_x(o2.get_x() - (o1.get_x() + o1.get_dim()[0] - o2.get_x() + o2.get_dim()[0]) - 1)
                if o1.get_y() + o1.get_dim()[1] < o2.get_y() - o2.get_dim()[1]:
                    o2.set_y(o2.get_y() + (o2.get_y() - o2.get_dim()[1] - o1.get_y() - o1.get_dim()[1]) + 1)
                o1.set_dir(Vecteur(0.0,0.0,0.0).sub(o1.get_dir()))  
                o2.set_dir(Vecteur(0.0,0.0,0.0).sub(o2.get_dir()))

    def sauvegarder_arene(self):
        with open('save.txt', 'wb') as save:
            arene = pickle.Pickler(save)
            arene.dump(self.dimx)
            arene.dump(self.dimy)
            arene.dump(self.objet)
            arene.dump(self.robot)

    def ouvrir_arene(self):

        try:

            with open('save.txt', 'rb') as save:
                arene_pickle = pickle.Unpickler(save)
                self.dimx = arene_pickle.load() 
                self.dimy = arene_pickle.load() 
                self.objet = arene_pickle.load() 
                self.robot = arene_pickle.load()

        except FileNotFoundError:
            pass
