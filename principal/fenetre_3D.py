# !/usr/bin/env python3
# -- coding: utf-8 -

import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.graphics import *

class Ligne():
    def __init__(self, x1, y1, x2, y2):
        self.vertex_list = pyglet.graphics.vertex_list(2, ('v2f', [x1, y1, x2, y2]), ('c3B', [0, 0, 0] * 2))

class Carre():
    def __init__(self, x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4):
        self.vertex_list = pyglet.graphics.vertex_list(4, ('v3f', [x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4]), \
            ('c3B', [0, 0, 0] * 4))

class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        glClearColor(1, 1, 1, 1)
        self.ligne = Ligne(500, 500, 200, 200)
        self.carre = Carre(600, 600, 600, 400, 400, 300, 500, 500, 300, 300, 300, 200)
        
    def on_draw(self):
        self.clear()
        self.ligne.vertex_list.draw(GL_LINES)
        self.ligne.vertex_list.draw(GL_QUADS)

if __name__ == '__main__':
    window = Window(1000, 600, "Robot 2I013")
    pyglet.app.run()