# !/usr/bin/env python3
# -- coding: utf-8 -

import pyglet
from pyglet.gl import *
from pyglet.window import key
from OpenGL.GLUT import *
from OpenGL.GL import glLight
from pyglet.image.codecs.png import PNGImageDecoder

class Window(pyglet.window.Window):
    xRotation = yRotation = 0
    increment = 5
    toDraw = []
    zoom = 2

    def setup(self):
        glClearColor(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1, 0, 0)
        glEnable(GL_DEPTH_TEST)
        glViewport(0, 0, super(Window, self).width * 2, super(Window, self).height * 2)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        aspectRatio = super(Window, self).width / super(Window, self).height
        gluPerspective(35 * self.zoom, aspectRatio, 1, 1000)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def setup_light(self):
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHT1)

        def vec(*args):
            return (GLfloat * len(args)) (*args)

        glLightfv(GL_LIGHT0, GL_POSITION, vec(0.5, 0.5, 1, 0))
        glLightfv(GL_LIGHT0, GL_SPECULAR, vec(0.5, 0.5, 1, 1))
        glLightfv(GL_LIGHT0, GL_DIFFUSE, vec(1, 1, 1, 1))
        glLightfv(GL_LIGHT1, GL_POSITION, vec(1, 0, 0.5, 0))
        glLightfv(GL_LIGHT1, GL_DIFFUSE, vec(0.5, 0.5, 0.5, 1))
        glLightfv(GL_LIGHT1, GL_SPECULAR, vec(1, 1, 1, 1))

        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, vec(0.5, 0.5, 0.5, 1))
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, vec(1, 1, 1, 1))
        glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, 50)

    def on_draw(self):
        self.clear()
        self.set_camera()
        glPushMatrix()

        glRotatef(self.xRotation, 1, 0, 0)
        glRotatef(self.yRotation, 0, 1, 0)

        for c in self.toDraw:
            c.draw()

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

    def on_text(self, text):
        print(self.zoom)
        if (text.find('z') > -1):
            self.zoom *= 0.75
        elif (text.find('Z') > -1):
            self.zoom *= 1.15
        elif (text.find('i') > -1):
            pyglet.image.get_buffer_manager().get_color_buffer().save('screenshot.png')

    def set_camera(self):
        # using Projection mode
        glViewport(0, 0, super(Window, self).width * 2, super(Window, self).height * 2)
        # taille de la scene
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        # perspective
        aspectRatio = super(Window, self).width / super(Window, self).height
        gluPerspective(35 * self.zoom, aspectRatio, 1, 1000)
        #
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(-200, -200, 0, 200, 200, -100, 0, 0, 1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup()

class Coord():
    def __init__(self, x, y, z, r, g, b):
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        self.g = g
        self.b = b
        self.cote = 20

    def draw(self):
        glBegin(GL_QUADS)
        glColor3ub(self.r, self.g, self.b) # couleur
        glVertex3f(self.x, self.y, self.z) # point 1
        glVertex3f(self.x+self.cote, self.y, self.z) # point 2
        glVertex3f(self.x+self.cote, self.y + self.cote, self.z) # ...
        glVertex3f(self.x, self.y+self.cote, self.z)
        glEnd()

class CoordTex(Coord):
    def __init__(self,x,y,z,r,g,b, fname):
        Coord.__init__(self, x, y, z, r, g, b)
        im = pyglet.image.load(fname, decoder = PNGImageDecoder())
        self.texture = im.get_texture()

    def draw(self):
        glBindTexture(self.texture.target, self.texture.id)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glBegin(GL_QUADS)
        glTexCoord2f(0,0)
        glVertex3f(self.x, self.y, self.z)
        glTexCoord2f(1, 0)
        glVertex3f(self.x + self.cote, self.y, self.z)
        glTexCoord2f(1, 1)
        glVertex3f(self.x + self.cote, self.y + self.cote, self.z)
        glTexCoord2f(0, 1)
        glVertex3f(self.x, self.y + self.cote, self.z)
        glEnd()
        glBindTexture(GL_TEXTURE_2D, 0)

if __name__ == '__main__':

    WINDOW = 400
    w = Window(WINDOW, WINDOW, 'Pyglet Colored Cube')
    w.toDraw += [Coord(0, 0, 0, 100, 0, 0)]
    w.toDraw += [Coord(0, 40, 0, 0, 255, 0)]
    w.toDraw += [Coord(50, 0, 0, 0, 0, 255)]
    pyglet.app.run()

    """
    window = Window(width = 1000, height = 600, caption = "Robot 2I013")
    pyglet.app.run()
    """