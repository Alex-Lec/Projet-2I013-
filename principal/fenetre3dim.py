# !/usr/bin/env python3
# -- coding: utf-8 -

import pyglet
from pyglet.gl import *
from pyglet.window import key
from OpenGL.GLUT import *
from OpenGL.GL import glLight
from pyglet.image.codecs.png import PNGImageDecoder

class Carre():
    def __init__(self, x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4):
        self.vertex_list = pyglet.graphics.vertex_list(4, ('v3f', [x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4]), \
            ('c3B', [0, 0, 0] * 4))

class Cube():
    def __init__(self, x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4, x5, y5, z5, x6, y6, z6, x7, y7, z7, x8, y8, z8):
        self.vertex_list = pyglet.graphics.vertex_list(20, ('v3f', [x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4, \
            x5, y5, z5, x6, y6, z6, x7, y7, z7, x8, y8, z8, \
                x1, y1, z1, x5, y5, z5, x6, y6, z6, x2, y2, z2, \
                    x1, y1, z1, x5, y5, z5, x8, y8, z8, x4, y4, z4, \
                        x2, y2, z2, x6, y6, z6, x7, y7, z7, x3, y3, z3]), \
                            ('c3B', [0, 0, 0] * 20))

class Ligne():
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.vertex_list = pyglet.graphics.vertex_list(2, ('v3f', [x1, y1, z1, x2, y2, z2]), ('c3B', [0, 0, 0] * 2))

class Window(pyglet.window.Window):
    xRotation = yRotation = 0
    increment = 5
    zoom = 2
    toDraw = []

    def setup(self):
        self.clear()
        glClearColor(0.80, 0.80, 0.80, 1)
        glClear(GL_COLOR_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)
        glViewport(0, 0, self.width, self.height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(35 * self.zoom, self.width / self.height, 0.5, 5000)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def setup2D(self): 
        glClearColor(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0, self.width, 0, self.height)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def on_draw(self):
        self.clear()
        glPushMatrix()

        glRotatef(self.xRotation, 1, 0, 0)
        glRotatef(self.yRotation, 0, 1, 0)
        
        self.carre.vertex_list.draw(GL_QUADS)
        self.cube.vertex_list.draw(GL_QUADS)
        self.ligne.vertex_list.draw(GL_LINES)
        
        """
        for c in self.toDraw:
            c.draw() 
        """

        glPopMatrix()

    def on_text_motion(self, motion):
        if (motion == key.UP):
            self.xRotation -= self.increment
        elif (motion == key.DOWN):
            self.xRotation += self.increment
        elif (motion == key.LEFT):
            self.yRotation -= self.increment
        elif (motion == key.RIGHT):
            self.yRotation += self.increment

    def on_resize(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(35 * self.zoom, width / height , 0.5, 5000)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(-500, -300, -1000)

    def on_text(self, text):
        print(self.zoom)
        if (text.find('z')>-1):
            self.zoom *= 0.75
        elif (text.find('Z')>-1):
            self.zoom *= 1.15
        elif (text.find('i')>-1):
            pyglet.image.get_buffer_manager().get_color_buffer().save('screenshot.png')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.toDraw += Carre(100, 100, 0, 200, 100, 0, 200, 200, 0, 100, 200, 0)
        self.carre = Carre(400, 400, 0, 500, 400, 0, 500, 500, 0, 400, 500, 0)
        self.cube = Cube(100, 100, 0, 200, 100, 0, 200, 200, 0, 100, 200, 0, \
            100, 100, -100, 200, 100, -100, 200, 200, -100, 100, 200, -100)
        self.ligne = Ligne(600, 300, 0, 700, 300, 0)
        self.setup()
        #self.setup2D()

if __name__ == '__main__':
    window = Window(width = 1000, height = 600, caption = 'Robot 2I013')
    pyglet.app.run()