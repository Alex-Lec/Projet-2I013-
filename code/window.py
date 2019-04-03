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
from composant import Robot, ObjetPhysique
from .terrain import Terrain
import time
from threading import Thread

class Carre():
    def __init__(self, x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4, red = 0, green = 0, blue = 0):
        self.vertex_list = pyglet.graphics.vertex_list(4, ('v3f', [x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4]), \
            ('c3B', [red, green, blue] * 4))

class Cube_test():
    def __init__(self, x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4, x5, y5, z5, x6, y6, z6, x7, y7, z7, x8, y8, z8, \
        red = 0, green = 0, blue = 0):
        self.vertex_list = pyglet.graphics.vertex_list(20, ('v3f', [x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4, \
            x5, y5, z5, x6, y6, z6, x7, y7, z7, x8, y8, z8, \
                x1, y1, z1, x5, y5, z5, x6, y6, z6, x2, y2, z2, \
                    x1, y1, z1, x5, y5, z5, x8, y8, z8, x4, y4, z4, \
                        x2, y2, z2, x6, y6, z6, x7, y7, z7, x3, y3, z3]), \
                            ('c3B', [red, green, blue] * 20))

class Ligne():
    def __init__(self, x1, y1, z1, x2, y2, z2, red = 0, green = 0, blue = 0):
        self.vertex_list = pyglet.graphics.vertex_list(2, ('v3f', [x1, y1, z1, x2, y2, z2]), ('c3B', [red, green, blue] * 2))

class Rectangle(ObjetPhysique):
    def __init__(self, *args, **kwargs):

        ObjetPhysique.__init__(self, *args, **kwargs)
        #Thread.__init__(self)

        x = self.x - self.largeur / 2
        y = self.y + self.hauteur / 2
        z = self.z - self.longueur / 2

        X = x + self.largeur
        Y = y + self.longueur
        Z = z + self.longueur

        color = ('c3B', (self.r, self.g, self.b) * 4)

        self.batch = pyglet.graphics.Batch()

        self.batch.add(4, GL_QUADS, None, ('v3f', (x,y,z, x,y,Z, x,Y,Z, x,Y,z)), color)
        self.batch.add(4, GL_QUADS, None, ('v3f', (X,y,Z, X,y,z, X,Y,z, X,Y,Z)), color)
        self.batch.add(4, GL_QUADS, None, ('v3f', (x,y,z, X,y,z, X,y,Z, x,y,Z)), color)
        self.batch.add(4, GL_QUADS, None, ('v3f', (x,Y,Z, X,Y,Z, X,Y,z, x,Y,z)), color)
        self.batch.add(4, GL_QUADS, None, ('v3f', (X,y,z, x,y,z, x,Y,z, X,Y,z)), color)
        self.batch.add(4, GL_QUADS, None, ('v3f', (x,y,Z, X,y,Z, X,Y,Z, x,Y,Z)), color)

    def draw(self):
        self.batch.draw()

"""
class Cube_tex(ObjetPhysique):
    def get_tex(self, file):
        tex = pyglet.image.load(file).texture
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        return pyglet.graphics.TextureGroup(tex)

    def __init__(self):
        ObjetPhysique.__init__(self, 0, 0, -1)

        #self.side = self.get_tex('texture.png')

        self.batch = pyglet.graphics.Batch()

        #tex_coords = ('t2f', (0, 0, 1, 0, 1, 1, 0, 1))

        x, y, z = 0, 0, -1
        X, Y, Z = x + 1, y + 1, z + 1

        color = ('c3B', (0, 0, 0) * 4)

        self.batch.add(4, GL_QUADS, None, ('v3f', (x,y,z, x,y,Z, x,Y,Z, x,Y,z)), color)
        self.batch.add(4, GL_QUADS, None, ('v3f', (X,y,Z, X,y,z, X,Y,z, X,Y,Z)), color)
        self.batch.add(4, GL_QUADS, None, ('v3f', (x,y,z, X,y,z, X,y,Z, x,y,Z)), color)
        self.batch.add(4, GL_QUADS, None, ('v3f', (x,Y,Z, X,Y,Z, X,Y,z, x,Y,z)), color)
        self.batch.add(4, GL_QUADS, None, ('v3f', (X,y,z, x,y,z, x,Y,z, X,Y,z)), color)
        self.batch.add(4, GL_QUADS, None, ('v3f', (x,y,Z, X,y,Z, X,Y,Z, x,Y,Z)), color)

        self.batch.add(4, GL_QUADS, self.side, ('v3f',(x,y,z, x,y,Z, x,Y,Z, x,Y,z)), tex_coords)
        self.batch.add(4, GL_QUADS, self.side, ('v3f',(X,y,Z, X,y,z, X,Y,z, X,Y,Z)), tex_coords)
        self.batch.add(4, GL_QUADS, self.side, ('v3f',(x,y,z, X,y,z, X,y,Z, x,y,Z)), tex_coords)
        self.batch.add(4, GL_QUADS, self.side, ('v3f',(x,Y,Z, X,Y,Z, X,Y,z, x,Y,z)), tex_coords)
        self.batch.add(4, GL_QUADS, self.side, ('v3f',(X,y,z, x,y,z, x,Y,z, X,Y,z)), tex_coords)
        self.batch.add(4, GL_QUADS, self.side, ('v3f',(x,y,Z, X,y,Z, X,Y,Z, x,Y,Z)), tex_coords)

    def draw(self):
        self.batch.draw()
"""

class Player(Robot):
    def __init__(self,pos=(0,0,0),rot=(0,0)):
        Robot.__init__(self, x= pos[0] , y = pos[1], z = pos[2])
        #Thread.__init__(self)

        self.pos = list(pos)
        self.rot = list(rot)

    def mouse_motion(self,dx,dy):
        dx /= 8; dy /= 8; self.rot[0] += dy; self.rot[1] -= dx
        if self.rot[0] > 90: self.rot[0] = 90
        elif self.rot[0]<-90: self.rot[0] = -90

    def update(self,dt,keys):
        s = dt*10
        rotY = -self.rot[1]/180*math.pi
        dx,dz = s*math.sin(rotY),s*math.cos(rotY)

        if (keys[key.Z]):
            self.pos[0]+=dx
            self.pos[2]-=dz

        if (keys[key.S]):
            self.pos[0]-=dx
            self.pos[2]+=dz

        if (keys[key.Q]):
            self.pos[0]-=dz
            self.pos[2]-=dx

        if (keys[key.D]):
            self.pos[0]+=dz
            self.pos[2]+=dx

        if (keys[key.SPACE]):
            self.pos[1]+=s

        if (keys[key.LSHIFT]):
            self.pos[1]-=s

class Window(pyglet.window.Window):

    toDraw = []

    def push(self,pos,rot): 
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
        
    lock = False
    mouse_lock = property(lambda self:self.lock,setLock)

    def __init__(self, arene = Terrain(), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)
        pyglet.clock.schedule(self.update)

        self.arene = arene
        self.tps = 25

        self.toDraw.append(Rectangle(x = 0, y = 0, z = -1, largeur = 1, longueur = 1, hauteur = 1, r = 0, g = 0, b = 0))
        self.toDraw.append(Rectangle(x = 10, y = 10, z = -10, largeur = 10, longueur = 10, hauteur = 10, r = 0, g = 0, b = 0))

        self.player = Player((0.5, 1.5, 1.5), (0,0))
        
        glClearColor(0.8, 0.8, 0.8, 1) 
        glEnable(GL_DEPTH_TEST)

        pyglet.app.run()

    def on_mouse_motion(self,x,y,dx,dy):
        if self.mouse_lock: self.player.mouse_motion(dx,dy)

    def on_key_press(self,KEY,MOD):
        if (KEY == key.ESCAPE):
            self.close()
        elif (KEY == key.E):
            self.mouse_lock = not self.mouse_lock

    def update(self,dt):
        self.player.update(dt,self.keys)

    def on_draw(self):
        self.clear()
        self.set3d()
        self.push(self.player.pos,self.player.rot)

        for c in self.toDraw:
            c.draw()

        glPopMatrix()

    def on_text(self, text):
        if (text.find('p') > -1 or text.find('P') > - 1):
            pyglet.image.get_buffer_manager().get_color_buffer().save('screenshot.png')
            print("Screenshot success !")

"""
if __name__ == '__main__':
    window = Window(width = 1000, height = 600, caption = 'Robot 2I013')
    #glEnable(GL_CULL_FACE)
    pyglet.app.run()
"""