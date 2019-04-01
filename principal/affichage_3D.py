# !/usr/bin/env python3
# -- coding: utf-8 -

import pyglet
from OpenGL.GL import glLight
from pyglet.gl import *
from pyglet.window import key
from OpenGL.GLUT import *
from pyglet.image.codecs.png import PNGImageDecoder

class Carre():
    def __init__(self, x1, y1, z1, x2, y2, z2, x3, y3, x4, y4, z4):
        vertex_list = pyglet.graphics.vertex_list(4, ('v3f', [x1, y1, z1, x2, y2, z2, x3, y3, x4, y4, z4]), \
            ('c3B', [255, 255, 255 * 4]))

class Affichage_3D(pyglet.window.Window):
    xRotation = yRotation = 0
    increment = 5
    toDraw = []

    def __init__(self, width, height, title='Test'):
        super(Affichage_3D, self).__init__(width, height, title)
        self.zoom = 20
        self.setup()


    def setup(self):
        # One-time GL setup
        glClearColor(1, 1, 1, 1)
        glColor3f(1, 0, 0)
        glEnable(GL_DEPTH_TEST)
        # using Projection mode
        glViewport(0, 0, super(Affichage_3D, self).width*2, \
        super(Affichage_3D, self).height*2) # taille de la scene
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        # perspective
        aspectRatio = super(Affichage_3D, self).width / \
                      super(Affichage_3D, self).height
        gluPerspective(35*self.zoom, aspectRatio, 1, 1000)
        #
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def setup_light(self):
        # Simple light setup. On Windows GL_LIGHT0 is enabled by default,
        # but this is not the case on Linux or Mac, so remember to always
        # include it.
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHT1)
        # Define a simple function to create ctypes arrays of floats:

        def vec(*args):
            return (GLfloat * len(args))(*args)

        glLightfv(GL_LIGHT0, GL_POSITION, vec(.5, .5, 1, 0))
        glLightfv(GL_LIGHT0, GL_SPECULAR, vec(.5, .5, 1, 1))
        glLightfv(GL_LIGHT0, GL_DIFFUSE, vec(1, 1, 1, 1))
        glLightfv(GL_LIGHT1, GL_POSITION, vec(1, 0, .5, 0))
        glLightfv(GL_LIGHT1, GL_DIFFUSE, vec(.5, .5, .5, 1))
        glLightfv(GL_LIGHT1, GL_SPECULAR, vec(1, 1, 1, 1))
        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, \
        vec(0.5, 0.5, 0.5, 1))
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, vec(1, 1, 1, 1))
        glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 50)

    def on_draw(self):
        # Clear the current GL Window
        self.clear()
        #self.set_camera() # cf plus tard
        # Push Matrix onto stack
        glPushMatrix()
        glRotatef(self.xRotation, 1, 0, 0)
        glRotatef(self.yRotation, 0, 1, 0)
        
        for c in self.toDraw:
            # Draw the six sides of the cube
            c.draw()
            
        # Pop Matrix off stack
        glPopMatrix()

if __name__ == '__main__':
    window = Affichage_3D(width = 1000, height = 600, title = "Robot 2I013")
    pyglet.app.run() 
