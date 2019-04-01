# !/usr/bin/env python3
# -- coding: utf-8 -

import pyglet
from pyglet.gl import *
from pyglet.window import key
from OpenGL.GLUT import *

INCREMENT = 5

class Ligne3D():
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.vertex_list = pyglet.graphics.vertex_list(2, ('v3f',  [x1, y1, z1, x2, y2, z2]), ('c3B', [0, 0, 0] * 2)) 

class Window(pyglet.window.Window):

    xRotation = yRotation = 30

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        glClearColor(1, 1, 1, 1)
        self.ligne3D = Ligne3D(500, 500, 0, 200, 200, 0)

    def on_draw(self):
        self.clear()
        self.ligne3D.pyglet.graphics.draw(GL_LINES)

    def on_rezize(self):
        glViewport(0, 0, self.width, self.height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(70, self.width / self.height, 0.05, 1000)
        glMatrixMode(GL_MODELVIEW)

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