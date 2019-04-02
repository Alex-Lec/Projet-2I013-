# !/usr/bin/env python3
# -- coding: utf-8 -

import pyglet
from pyglet.gl import *
from pyglet.window import key
from OpenGL.GLUT import *
from OpenGL.GL import glLight
from pyglet.image.codecs.png import PNGImageDecoder
from PIL import Image
import random
import numpy

if __name__ == '__main__':
    img = Image.open("screenshot.png")
    print(img.size, img.format)
    #img.show()
    data = list(img.getdata())
    #print(data[:10])
    r = [i[0] for i in data]
    print(r[0])
    for i in range(len(r)):
        if (r[i] == 255):
            data[i] = (0, 0, 0, 255)
    imgNew = Image.new(img.mode, img.size)
    imgNew.putdata(data)
    imgNew.show()

"""
if __name__ == '__main__':
    d = 512
    img = Image.new("RGB", (d, d), "white")

    for i in range(d):
        for j in range(d):
            img.putpixel((i, j), (0, 255, 0))

    for i in range(15000):
        img.putpixel((random.randint(0, d - 1), random.randint(0, d - 1)), \
            (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    for i in range(50):
        for j in range(50):
            img.putpixel((i + 50, j + 50), (255, 0, 0))

    img.save("matexture.png", "png")
    print(img.getpixel((10, 10)))
    numpy.array(img)
"""