# !/usr/bin/env python3
# -- coding: utf-8 -

import pyglet
from pyglet.gl import *
from pyglet.window import key
from OpenGL.GLUT import *
from OpenGL.GL import glLight
from pyglet.image.codecs.png import PNGImageDecoder
import math
import random
import numpy
from .terrain import Terrain
from composant import Rectangle, Vecteur, Sol, Player
import time
from threading import Thread
import numpy as np
import vg
from PIL import Image


class Affichage_3D(pyglet.window.Window, Thread):

    toDraw = []

    def push(self, pos, rot):

        """
        Définie la matrice de translation
        """

        glPushMatrix()
        glRotatef(-rot[0],1,0,0)
        glRotatef(-rot[1],0,1,0)
        glTranslatef(-pos[0],-pos[1],-pos[2])

    def Projection(self): 
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

    def Model(self): 
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def set3d(self): 

        """
        Définie la 3D souhaitée
        Perspective, ratio, distance de rendu minimal et maximal
        """

        self.Projection()
        gluPerspective(70, self.width / self.height, 0.05, 5000)
        self.Model()

    def setLock(self,state): 
        self.lock = state
        self.set_exclusive_mouse(state)

    def unit_vector(self, vector):
        return vector / np.linalg.norm(vector)
      
    def angle_between_2_vectors(self, v1, v2):

        """
        Permet de calculer l'angle en degré entre le vecteur fixe y = (0, 1, 0) et le vecteur direction du robot
        """

        v1_u = self.unit_vector(v1)
        v2_u = self.unit_vector(v2)
        return np.rad2deg(np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0)))

    lock = False
    mouse_lock = property(lambda self:self.lock,setLock)

    def __init__(self, arene, *args, **kwargs):
        pyglet.window.Window.__init__(self, *args, **kwargs)
        Thread.__init__(self)

        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)

        self.arene = arene
        rob = self.arene.robot[0]
        self.tps = 25

        self.vecteur_y = Vecteur(0., 1., 0.)

        # Ajoute la représentation graphique représentant le sol de l'arène
        self.toDraw.append(Sol())
        for i in self.arene.objet[4:]:
            self.toDraw.append(Rectangle(i.x, i.z, i.y, i.longueur,\
            i.largeur, i.hauteur, 0, 0, 255))

        if (rob.v_dir.x < 0 or rob.v_dir.y < 0):
            self.player = Player((rob.x, rob.z + 1, rob.y), (0, 180 - self.angle_between_2_vectors(self.vecteur_y.vector, rob.v_dir.vector)), rob.largeur, rob.longueur, rob.hauteur)
        else:
            self.player = Player((rob.x, rob.z + 1, rob.y), (0, 180 + self.angle_between_2_vectors(self.vecteur_y.vector, rob.v_dir.vector)), rob.largeur, rob.longueur, rob.hauteur)
    
        # Définie la couleur de fond de la fenêtre
        glClearColor(0.8, 0.8, 0.8, 1) 
        glEnable(GL_DEPTH_TEST)

    def run(self):
        pyglet.clock.schedule(self.update)
        pyglet.app.run()

    def on_mouse_motion(self,x,y,dx,dy):
        if self.mouse_lock: self.player.mouse_motion(dx,dy)

    def on_key_press(self,KEY,MOD):

        """
        Permet lorsque l'on presse la touche 'E' de passer en caméra libre ou de revenir en caméra fixe
        """

        if (KEY == key.ESCAPE):
            self.close()
        elif (KEY == key.E):
            self.mouse_lock = not self.mouse_lock
            rob = self.arene.robot[0]
            if (self.mouse_lock == False):
                self.arene.update()
                rob = self.arene.robot[0]
                self.player.rot[0] = 0
                if (rob.v_dir.x < 0 or rob.v_dir.y < 0):
                    self.player.rot[1] = 180 - self.angle_between_2_vectors(self.vecteur_y.vector, rob.v_dir.vector)
                else:
                    self.player.rot[1] = 180 + self.angle_between_2_vectors(self.vecteur_y.vector, rob.v_dir.vector)

    def update(self,dt):

        """
        Permet de mettre à jour la position et l'orientation de la caméra
        """

        self.player.update(dt,self.keys)
        self.arene.update()

        rob = self.arene.robot[0]

        self.player.pos[0] = rob.x
        self.player.pos[1] = rob.z + 1
        self.player.pos[2] = rob.y

        if (self.mouse_lock == False):
            if (rob.v_dir.x < 0 or rob.v_dir.y < 0):
                self.player.rot[1] = 180 - self.angle_between_2_vectors(self.vecteur_y.vector, rob.v_dir.vector)
            else:
                self.player.rot[1] = 180 + self.angle_between_2_vectors(self.vecteur_y.vector, rob.v_dir.vector)

        print(rob.v_dir.vector)

    def on_draw(self):

        """
        Affiche les éléments de l'arène
        """

        self.clear()
        self.set3d()
        self.push(self.player.pos,self.player.rot)

        for c in self.toDraw:
            c.draw()

        glPopMatrix()

    def on_text(self, text):

        """
        Permet de prendre un screenshot de la fenêtre à la volée
        """

        if (text.find('p') > -1 or text.find('P') > -1):
            pyglet.image.get_buffer_manager().get_color_buffer().save('image.jpeg')
            img = Image.open('image.jpeg')
            rbg_img = img.convert('RGB')
            rbg_img.save('image.jpeg')
            print("Screenshot success !")

    def screenshot(self):

        """
        Permet de prendre un screenshot de la fenêtre
        Peut être appelée depuis un controleur
        Utile pour la simulation de traitement d'image
        """

        pyglet.image.get_buffer_manager().get_color_buffer().save('image.jpeg')
        img = Image.open('image.jpeg')
        rbg_img = img.convert('RGB')
        rbg_img.save('image.jpeg')
