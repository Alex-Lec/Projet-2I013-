# -*- coding: utf-8 -*-
import time

class Roue:
    def __init__(self, retour, rotation):
        self.retour = retour
        self.rotation = rotation

   # def Tourner(self, angle):
     #   pass

    def Tourner(self, unite):
        t0=time.clock()
        tf=time.clock()
        while (tf<t0+unite):
            print(t0, tf)
            #active une roue du robot pour une "unité de rotation"
            #(à définir en radians)

            tf=time.clock()
