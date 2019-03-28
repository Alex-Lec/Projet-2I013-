# !/usr/bin/env python3
# -- coding: utf-8 -

import pyglet
from pyglet.gl import *
from pyglet.window import key
from OpenGL.GLUT import *

class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        self