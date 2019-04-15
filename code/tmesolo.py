#!/usr/bin/env python3
# -*- coding: utf-8 -*

q1.1():

"""
On peut tester cette fonction en exécutant le main et en choissant le controleur_carre et le simulateur 2D
"""

    for r in self.arene.robot:
        tag_robot = "robot_" + str(self.arene.robot.index(r))
        self.canvas.delete(tag_robot)
        
        self.canvas.create_polygon(r.get_points(), fill = "pink", tags = tag_robot)
        self.canvas.create_text(r.x, r.y, text = self.arene.robot.index(r) + 1, \
                                fill = "black", tags = tag_robot)

        self.canvas.create_line(r.x + r.v_dir.x * 20, r.y + \
                                r.v_dir.y * 20, r.x + r.v_dir.x * 40, r.y + \
                                r.v_dir.y * 40, fill = "black", tags = tag_robot)
    self.fenetre.after(5,self.update_robots)

q1.2():
"""
On peut tester cette fonction en exécutant le main et en choissant le controleur_carre et le simulateur 2D
"""

    for r in self.arene.robot:
        tag_robot = "robot_" + str(self.arene.robot.index(r))
        self.canvas.delete(tag_robot)

        self.canvas.create_polygon(r.get_points(), fill = "grey")

        self.canvas.create_polygon(r.get_points(), fill = "pink", tags = tag_robot)
        self.canvas.create_text(r.x, r.y, text = self.arene.robot.index(r) + 1, \
                                fill = "black", tags = tag_robot)

        self.canvas.create_line(r.x + r.v_dir.x * 20, r.y + \
                                r.v_dir.y * 20, r.x + r.v_dir.x * 40, r.y + \
                                r.v_dir.y * 40, fill = "black", tags = tag_robot)
    self.fenetre.after(5,self.update_robots)

q2.1():
"""
On peut tester cette fonction en exécutant le main et en choisissant le controleur_triangle et le simulateur 2D (ou 3D)
"""

from strategie import StratAvanceplus,StratStop,StratTourneplus
from threading import Thread
import time

class Controleur_triangle():
    def __init__(self,rob,dst = 100,vit = 500):
        self.robot = rob
        self.cnt = 0
        self.Go = None
        self.vitesse = vit
        self.dst = dst

    def start(self):
        self.Go = StratAvanceplus(self.robot,self.dst,self.vitesse)
        self.Go.start()
        self.cnt = 0

    def step(self):
        self.Go.step()

        if (self.Go.stop()):
            print(type(self.Go).__name__)
            if (type(self.Go).__name__ == "StratAvanceplus") :#switch strategie
                self.Go = StratTourneplus(self.robot,120,100)
                self.cnt +=1

            elif (type(self.Go).__name__ == 'StratTourneplus') :#switch strategie
                self.Go = StratAvanceplus(self.robot,self.dst,self.vitesse)

            self.Go.start()

    def stop(self):
        if (self.cnt >= 3):
            self.Go = StratStop(self.robot)
            self.Go.start()
            return False
        return True

q2.2():
"""
On peut tester cette fonction en exécutant le main et en choisissant le controleur_polygones_n_cotes et le simulateur 2D (ou 3D)
"""


from strategie import StratAvanceplus,StratStop,StratTourneplus
from threading import Thread
import time
import math

class Controleur_polygone_n_cotes():
    def __init__(self, rob, dst = 300, vit = 500, nb_cotes = 4):
        self.robot = rob
        self.cnt = 0
        self.Go = None
        self.vitesse = vit
        self.dst = 300 / nb_cotes
        self.nb_cotes = nb_cotes
        self.angle = 180 - math.degrees(((nb_cotes - 2) * math.pi) / nb_cotes)

    def start(self):
        self.Go = StratAvanceplus(self.robot, self.dst, self.vitesse)
        self.Go.start()
        self.cnt = 0

    def step(self):
        self.Go.step()

        if (self.Go.stop()):
            print(type(self.Go).__name__)
            if (type(self.Go).__name__ == "StratAvanceplus") :#switch strategie
                self.Go = StratTourneplus(self.robot, self.angle, 100)
                print(self.angle)
                self.cnt +=1
                
            elif (type(self.Go).__name__ == 'StratTourneplus') :#switch strategie
                self.Go = StratAvanceplus(self.robot,self.dst,self.vitesse)
        
            self.Go.start()

    def stop(self):
        if (self.cnt >= self.nb_cotes):
            self.Go = StratStop(self.robot)
            self.Go.start()
            return False
        return True

q3.1():

"""
On peut tester cette fonction en choisissant le controleur_zones_grises et le simulateur 2D
"""

from .vecteur import Vecteur
import numpy as np
from math import radians,sqrt, cos, sin, pi

class Zones_Grises():

    def __init__(self, x = 0, y = 0, z = 0, largeur = 50, longueur = 100, hauteur = 20):
       
        self.x = x
        self.y = y
        self.z = z
        self.longueur = longueur
        self.largeur = largeur
        self.hauteur = hauteur
        self.v_dir = Vecteur(1., 0., 0.)
        self.vector = Vecteur(self.x, self.y, self.z)
        self.color = 'grey'

    def get_points(self):
    
        points = [[self.x -self.longueur//2, self.y - self.largeur//2],\
            [self.x + self.longueur//2, self.y - self.largeur//2],\
            [self.x + self.longueur//2, self.y + self.largeur//2],\
            [self.x - self.longueur//2, self.y + self.largeur//2]]


        VecteurDirection = (self.v_dir.x,self.v_dir.y,self.v_dir.z)
        v_direction =    VecteurDirection / np.linalg.norm(VecteurDirection)

        
        VecteurDefaut = (1,0,0)
        v_defaut = VecteurDefaut/np.linalg.norm(VecteurDefaut)

        if (self.v_dir.y > 0):
            angle = np.arccos(np.clip(np.dot(v_direction, v_defaut), -1.0, 1.0))
        else :
            angle = 2*pi-np.arccos(np.clip(np.dot(v_direction, v_defaut), -1.0, 1.0))

        cos_val = cos(angle)
        sin_val = sin(angle)

        new_points = []
        for x_old, y_old in points:
            x_old -= self.x
            y_old -= self.y
            x_new = x_old * cos_val - y_old * sin_val
            y_new = x_old * sin_val + y_old * cos_val
            new_points.append([x_new + self.x, y_new + self.y])
        
        return new_points         
                   
    def check_robot_zone(self, robot):
        if ((robot.x - robot.longueur//2, robot.y - robot.largeur//2 >= self.x -self.longueur//2, self.y - self.largeur//2 and \
            robot.x + robot.longueur//2, robot.y - robot.largeur//2 <= self.x + self.longueur//2, self.y - self.largeur//2) or \
                (robot.x + robot.longueur//2, robot.y + robot.largeur//2 >= self.x + self.longueur//2, self.y + self.largeur//2 and \
                    robot.x - robot.longueur//2, robot.y + robot.largeur//2 <= self.x - self.longueur//2, self.y + self.largeur//2):
            
            robot.vd /= 2
            robot.vg /= 2
            return True
        return False

q3.2():

"""
On peut tester cette fonction en choisissant le controleur_zones_grises et le simulateur 2D
"""
             
def detecte_all(self, angle):
    """
    Mesure la distance entre le devant du robot et les objets devant.
    Retourne seulement l'objet dans la bonne direction et le plus proche du robot
    DETECTE LES AUTRES ROBOTS
    
    NE MARCHE QUE SI ROBOT A UNE robot.arene !!!
    """

    if (self.robot.arene == None):
        return
    
    obj = self.robot.arene.objet + self.robot.arene.robot + self.robot.arene.zone_grises
    
    def mmsigne(a,b): 
        if (a<0 and b<0):
            return True
        if (a==0 and b==0):
            return True
        return (a>0 and b>0)
        
    mini = 1000000
    p1 = (self.robot.x,self.robot.y)
    p2 = (self.robot.x + (self.robot.longueur /2) * self.robot.v_dir.x * math.radians(angle),
            self.robot.y + (self.robot.longueur /2) * self.robot.v_dir.y)
    
    if (round(p1[0]-p2[0],12) != 0): 
        a1 = (p1[1] - p2[1]) /(p1[0]- p2[0])
        b1 = p1[1] - a1*p1[0]
    else :
        a1 = None # Cas ou le robot est dans l'axe x
        b1 = p1[0]
        
    for o in obj:
        if (o == self.robot):
            continue
            
        opt = o.get_points()
        for j in range(len(opt)):
            p3 = opt[j]
            p4 = opt[(j+1)%len(opt)]#Marche avec un polygone à n cotées
            
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
            
            res = sqrt(pow(p2[0]-x,2)+pow(p2[1]-y,2))
            
            if mmsigne(p2[0] - p1[0],x - p1[0]) and mmsigne(p2[1] - p1[1],y - p1[1]):
                
                if (min(p3[0],p4[0])<=x<=max(p3[0],p4[0]) and 
                    min(p3[1],p4[1])<=y<=max(p3[1],p4[1])):
                    
                    h = self.robot.z + (self.robot.hauteur/2)
                    
                    bobj = min(o.z, o.z + o.hauteur)
                    hobj = max(o.z, o.z + o.hauteur)
                    
                    if (h <= hobj and h >= bobj):
                        if (mini > res):
                            mini = res

    return mini

q3.3():

"""
On peut tester cette fonction en choisissant le controleur_zones_grises et le simulateur 2D
"""

arene.zones_grises.append(Zones_Grises(300, 25, 0, 50, 50, 50))
arene.zones_grises.append(Zones_Grises(300, 80, 0, 50, 50, 50))
arene.zones_grises.append(Zones_Grises(300, 135, 0, 50, 50, 50))

arene.zones_grises.append(Zones_Grises(300, 325, 0, 50, 50, 50))
arene.zones_grises.append(Zones_Grises(300, 380, 0, 50, 50, 50))
arene.zones_grises.append(Zones_Grises(300, 435, 0, 50, 50, 50))

arene.zones_grises.append(Zones_Grises(600, 135, 0, 50, 50, 50))
arene.zones_grises.append(Zones_Grises(600, 190, 0, 50, 50, 50))
arene.zones_grises.append(Zones_Grises(600, 245, 0, 50, 50, 50))

arene.zones_grises.append(Zones_Grises(600, 425, 0, 50, 50, 50))
arene.zones_grises.append(Zones_Grises(600, 480, 0, 50, 50, 50))
arene.zones_grises.append(Zones_Grises(600, 535, 0, 50, 50, 50))

arene.zones_grises.append(Zones_Grises(900, 25, 0, 50, 50, 50))
arene.zones_grises.append(Zones_Grises(900, 80, 0, 50, 50, 50))
arene.zones_grises.append(Zones_Grises(900, 135, 0, 50, 50, 50))

arene.zones_grises.append(Zones_Grises(900, 225, 0, 50, 50, 50))
arene.zones_grises.append(Zones_Grises(900, 280, 0, 50, 50, 50))
arene.zones_grises.append(Zones_Grises(900, 335, 0, 50, 50, 50))

arene.zones_grises.append(Zones_Grises(1200, 135, 0, 50, 50, 50))
arene.zones_grises.append(Zones_Grises(1200, 190, 0, 50, 50, 50))
arene.zones_grises.append(Zones_Grises(1200, 245, 0, 50, 50, 50))

arene.zones_grises.append(Zones_Grises(1200, 425, 0, 50, 50, 50))
arene.zones_grises.append(Zones_Grises(1200, 480, 0, 50, 50, 50))
arene.zones_grises.append(Zones_Grises(1200, 535, 0, 50, 50, 50))

arene.zones_grises.append(Zones_Grises(1350, 25, 0, 50, 50, 50))