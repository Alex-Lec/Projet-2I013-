# !/usr/bin/env python3
# -- coding: utf-8 -

import pyglet
from OpenGl.GL import glLight
from pyglet.gl import *
from pyglet.window import key
from OpenGL.GLUT import *
from pyglet.image.codecs.png import PNGImageDecoder

class Window(pyglet.window.Window):
    xRotation = yRotation = 0
    increment = 5
    toDraw = []

    def __init__(self, width, height, title='Test'):
        super(Window, self).__init__(width, height, title)
        self.setup()

    def setup(self):
        # One-time GL setup
        glClearColor(1, 1, 1, 1)
        glColor3f(1, 0, 0)
        glEnable(GL_DEPTH_TEST)
        # using Projection mode
        glViewport(0, 0, super(Window, self).width*2, \
        super(Window, self).height*2) # taille de la scene
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        # perspective
        aspectRatio = super(Window, self).width / \
        super(Window, self).height
        gluPerspective(35*self.zoom, aspectRatio, 1, 1000)
        #
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()