# !/usr/bin/env python3
# -- coding: utf-8 -

import pyglet
from pyglet.gl import *
from pyglet.window import key
from OpenGL.GLUT import *

"""
class Ligne():
    def __init__(self, x1, y1, x2, y2):
        self.vertex_list = pyglet.graphics.vertex_list(2, ('v2f', [x1, y1, x2, y2]), ('c3B', [0, 0, 0] * 2))

class Ligne3D():
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.vertex_list = pyglet.graphics.vertex_list(2, ('v3f', [x1, y1, z1, x2, y2, z2]), ('c3B', [0, 0, 0] * 2))

class Carre():
    def __init__(self, x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4):
        self.vertex_list = pyglet.graphics.vertex_list(4, ('v3f', [x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4]), \
            ('c3B', [0, 0, 0] * 4))

class Carre2D():
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.vertex_list = pyglet.graphics.vertex_list(4, ('v2f', [x1, y1, x2, y2, x3, y3, x4, y4]), \
            ('c3B', [0, 0, 0] * 4))

INCREMENT = 5
class Window(pyglet.window.Window):

    xRotation = yRotation = 30

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
        gluPerspective(70, self.width / self.height, 0.05, 1000)
        self.Model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        glClearColor(1, 1, 1, 1)

        self.ligne3D = Ligne3D(500, 500, -100, 200, 200, -200)

        
        glEnable(GL_DEPTH_TEST)  
        self.ligne = Ligne(500, 500, 200, 200)
        self.ligne3D = Ligne3D(500, 500, -100, 200, 200, -200)
        self.carre2D = Carre2D(300, 300, 400, 300, 400, 400, 300, 400)
        self.carre = Carre(300, 300, -100, 400, 300, -100, 400, 400, -100, 300, 400, -100)
        
    @window_event 
    def on_draw(self):
        self.clear()
        #self.set2d()
        #self.set3d()
        glDrawArrays(GL_LINES, 0, 3)

    @window_event
    def on_rezize(self):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(70, width / height, 0.05, 1000)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def on_text_motion(self, motion):
        if motion == key.UP:
            self.xRotation -= INCREMENT

        elif motion == key.DOWN:
            self.xRotation += INCREMENT

        elif motion == key.LEFT:
            self.yRotation -= INCREMENT

        elif motion == key.RIGHT:
            self.yRotation += INCREMENT

if __name__ == '__main__':
    window = Window(width = 1000, height = 600, caption = "Robot 2I013")
    pyglet.app.run()
"""

WINDOW    = 400
INCREMENT = 5

class Window(pyglet.window.Window):

    # Cube 3D start rotation
    xRotation = yRotation = 30  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #glClearColor(1, 1, 1, 1)
        glEnable(GL_DEPTH_TEST)  

    def on_draw(self):
        # Clear the current GL Window
        self.clear()

        # Push Matrix onto stack
        glPushMatrix()

        glRotatef(self.xRotation, 1, 0, 0)
        glRotatef(self.yRotation, 0, 1, 0)

        # Draw the six sides of the cube
        glBegin(GL_QUADS)

        # White
        glColor3ub(255, 255, 255)
        glVertex3f(50,50,50)

        # Yellow
        glColor3ub(255, 255, 0)
        glVertex3f(50,-50,50) 

        # Red
        glColor3ub(255, 0, 0)
        glVertex3f(-50,-50,50)
        glVertex3f(-50,50,50)

        # Blue
        glColor3f(0, 0, 1)
        glVertex3f(-50,50,-50) 

        glEnd()

        # Pop Matrix off stack
        glPopMatrix()

    def on_resize(self, width, height):
        # set the Viewport
        glViewport(0, 0, width, height)

        # using Projection mode
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        aspectRatio = width / height
        gluPerspective(35, aspectRatio, 1, 1000)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0, 0, -400)

    def on_text_motion(self, motion):
        if motion == key.UP:
            self.xRotation -= INCREMENT
        elif motion == key.DOWN:
            self.xRotation += INCREMENT
        elif motion == key.LEFT:
            self.yRotation -= INCREMENT
        elif motion == key.RIGHT:
            self.yRotation += INCREMENT

if __name__ == '__main__':
   Window(WINDOW, WINDOW, 'Pyglet Colored Cube')
   pyglet.app.run()