#! /usr/bin/env/python3
# -- coding: utf-8 -

import time
import numpy
import sys

class StratGetImage():
    def __init__(self, rob):
        self.robot = rob

    def start(self):
        self.robot.get_image()

    def step(self):
        pass
    
    def stop(self):
        return False