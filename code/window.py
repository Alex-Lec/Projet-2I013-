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
from composant import ObjetPhysique, Vecteur
from .terrain import Terrain
import time
from threading import Thread
import numpy as np
import vg
from PIL import Image

class Rectangle():
    def __init__(self, x, y, z, largeur, longueur, hauteur, r, g, b):

        self.x = x
        self.y = y
        self.z = z
        self.largeur = largeur
        self.longueur = hauteur
        self.hauteur = longueur

        x = self.x - self.largeur / 2
        y = self.y
        z = self.z - self.longueur / 2

        X = x + self.largeur
        Y = y + self.hauteur
        Z = z + self.longueur

        color = ('c3B', (r, g, b) * 4)

        self.batch = pyglet.graphics.Batch()

        self.batch.add(4, GL_QUADS, None, ('v3f', (x,y,z, x,y,Z, x,Y,Z, x,Y,z)), color)
        self.batch.add(4, GL_QUADS, None, ('v3f', (X,y,Z, X,y,z, X,Y,z, X,Y,Z)), color)
        self.batch.add(4, GL_QUADS, None, ('v3f', (x,y,z, X,y,z, X,y,Z, x,y,Z)), color)
        self.batch.add(4, GL_QUADS, None, ('v3f', (x,Y,Z, X,Y,Z, X,Y,z, x,Y,z)), color)
        self.batch.add(4, GL_QUADS, None, ('v3f', (X,y,z, x,y,z, x,Y,z, X,Y,z)), color)
        self.batch.add(4, GL_QUADS, None, ('v3f', (x,y,Z, X,y,Z, X,Y,Z, x,Y,Z)), color)

    def draw(self):
        self.batch.draw()

class Sol():
    def __init__(self, x = 750, y = 450, z = 0, largeur = 5000, longueur = 5000, hauteur = 1, \
        r = 255, g = 255, b = 255):

        color = ('c3B', (r, g, b) * 4)
        color_lines = ('c3B', (0, 0, 0) * 2)

        self.batch = pyglet.graphics.Batch()

        hauteur = 150

        self.batch.add(4, GL_QUADS, None, ('v3f', (0,0,0, 0,0,900, 1500,0,900, 1500,0,0)), color)
        self.batch.add(2, GL_LINES, None, ('v3f', (0,hauteur,0, 1500,hauteur,900)), color_lines)
        self.batch.add(2, GL_LINES, None, ('v3f', (0,hauteur,900, 1500,hauteur,0)), color_lines)
        self.batch.add(2, GL_LINES, None, ('v3f', (0,hauteur,0, 1500,hauteur,0)), color_lines)
        self.batch.add(2, GL_LINES, None, ('v3f', (0,hauteur,0, 0,hauteur,900)), color_lines)
        self.batch.add(2, GL_LINES, None, ('v3f', (1500,hauteur,0, 1500,hauteur,900)), color_lines)
        self.batch.add(2, GL_LINES, None, ('v3f', (0,hauteur,900, 1500,hauteur,900)), color_lines)
   
    def draw(self):
        self.batch.draw()

class Player():
    def __init__(self,pos=(0,0,0),rot=(0,0), largeur = 1, longueur = 1, hauteur = 1):

        self.pos = list(pos)
        self.rot = list(rot)
        self.largueur = largeur
        self.longueur = hauteur
        self.hauteur = longueur
        
    def mouse_motion(self,dx,dy):
        dx /= 8; dy /= 8; self.rot[0] += dy; self.rot[1] -= dx
        if self.rot[0] > 90: self.rot[0] = 90
        elif self.rot[0]<-90: self.rot[0] = -90

    def update(self,dt,keys):
        s = dt*20
        rotY = -self.rot[1]/180*math.pi
        dx,dz = s*math.sin(rotY),s*math.cos(rotY)

        if (keys[key.Z]):
            self.pos[0]+=dx*10
            self.pos[2]-=dz*10

        if (keys[key.S]):
            self.pos[0]-=dx*10
            self.pos[2]+=dz*10

        if (keys[key.Q]):
            self.pos[0]-=dz*10
            self.pos[2]-=dx*10

        if (keys[key.D]):
            self.pos[0]+=dz*10
            self.pos[2]+=dx*10

        if (keys[key.SPACE]):
            self.pos[1]+=s

        if (keys[key.LSHIFT]):
            self.pos[1]-=s

class Window(pyglet.window.Window, Thread):

    toDraw = []

    def push(self, pos, rot):
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

    def set2d(self): 
        self.Projection()
        gluOrtho2D(0, self.width, 0, self.height)
        self.Model()

    def set3d(self): 
        self.Projection()
        gluPerspective(70, self.width / self.height, 0.05, 5000)
        self.Model()

    def setLock(self,state): 
        self.lock = state
        self.set_exclusive_mouse(state)

    def unit_vector(self, vector):
        return vector / np.linalg.norm(vector)
      
    def angle_between_2_vectors(self, v1, v2):
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

        self.toDraw.append(Sol())
        #self.toDraw.append(Rectangle(x = 1000, y = 0, z = 100, largeur = 10, longueur = 10, hauteur = 10, r = 0, g = 0, b = 255))
        self.toDraw.append(Rectangle(x = 500, y = 0, z = 200, largeur = 10, longueur = 10, hauteur = 10, r = 0, g = 0, b = 255))


        self.arene.objet.append(ObjetPhysique(x = 750, y = 450, z = 0, largeur = 5000, longueur = 5000, hauteur = 1, \
        r = 255, g = 255, b = 255))

        #self.arene.objet.append(ObjetPhysique(x = 1000, y = 100, z = 0, largeur = 10, longueur = 10, hauteur = 10))
        self.arene.objet.append(ObjetPhysique(x = 500, y = 200, z = 0, largeur = 10, longueur = 10, hauteur = 10))


        if (rob.v_dir.x < 0 or rob.v_dir.y < 0):
            self.player = Player((rob.x, rob.z + 1, rob.y), (0, 180 - self.angle_between_2_vectors(self.vecteur_y.vector, rob.v_dir.vector)), rob.largeur, rob.longueur, rob.hauteur)
        else:
            self.player = Player((rob.x, rob.z + 1, rob.y), (0, 180 + self.angle_between_2_vectors(self.vecteur_y.vector, rob.v_dir.vector)), rob.largeur, rob.longueur, rob.hauteur)
    
        glClearColor(0.8, 0.8, 0.8, 1) 
        glEnable(GL_DEPTH_TEST)

    def run(self):
        pyglet.clock.schedule(self.update)
        pyglet.app.run()

    def on_mouse_motion(self,x,y,dx,dy):
        if self.mouse_lock: self.player.mouse_motion(dx,dy)

    def on_key_press(self,KEY,MOD):
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

    def on_draw(self):
        self.clear()
        self.set3d()
        self.push(self.player.pos,self.player.rot)

        for c in self.toDraw:
            c.draw()

        #self.robToDraw.draw()

        glPopMatrix()

    def on_text(self, text):
        if (text.find('p') > -1 or text.find('P') > -1):
            pyglet.image.get_buffer_manager().get_color_buffer().save('image.jpeg')
            img = Image.open('image.jpeg')
            rbg_img = img.convert('RGB')
            rbg_img.save('image.jpeg')
            print("Screenshot success !")

    def screenshot(self):
        pyglet.image.get_buffer_manager().get_color_buffer().save('image.jpeg')
        img = Image.open('image.jpeg')
        rbg_img = img.convert('RGB')
        rbg_img.save('image.jpeg')