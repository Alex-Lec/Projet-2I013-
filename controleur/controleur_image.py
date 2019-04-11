#!/usr/bin/env python3
# -*- coding: utf-8 -*

from threading import Thread
from PIL import Image
import sys

class Controleur_image(Thread):
    def __init__(self, robot):
        Thread.__init__(self)
        self.robot = robot

    def start(self):
        self.robot.get_image()
        img = Image.open("test.jpeg")
        img.rotate(180)
        img.save("test_final.jpeg", "jpeg")

    def step(self):
        pass

    def stop(self):
        False 
