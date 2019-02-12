#!/usr/bin/env python3
# -- coding: utf-8 -

from Terrain import *
from tkinter import *
from Robot import *
import time

class Fenetre_test():

    def __init__(self, arene = Terrain()):
        
        self.fenetre = Tk()
        self.fenetre.title("Simulateur")
        self.fenetre.geometry("1000x600")
        self.fenetre.resizable(0, 0)
        self.arene = arene

        menubar = Menu(self.fenetre)

        menu0 = Menu(menubar, tearoff= 0)
        menu0.add_command(label = "Ouvrir")
        menu0.add_command(label = "Enregistrer")
        menu0.add_separator()
        menu0.add_command(label = "Quitter", command = self.fenetre.destroy)
        menubar.add_cascade(label = "Fichier", menu = menu0)

        menu1 = Menu(menubar, tearoff = 0)
        menu1.add_command(label = "Créer robot", command = self.creerRobot)
        menu1.add_command(label = "Créer objet", command = self.creerObjet)
        menubar.add_cascade(label = "Création", menu = menu1)

        menu2 = Menu(menubar, tearoff = 0)
        menu2.add_command(label = "Tourner robot", command = self.tournerRobot)
        menu2.add_command(label = "Déplacer robot", command = self.deplacerRobot)
        menubar.add_cascade(label = "Déplacement", menu = menu2)

        self.fenetre.config(menu = menubar)

        self.arene_canvas = Canvas(self.fenetre, width = 1000, height = 600)
        self.arene_canvas.pack()

        self.initialise_arene()
        self.fenetre.mainloop()

    def initialise_arene(self):

        for o in self.arene.objet:
            #tag_objet = "objet_" + str(self.arene.object.index(o))
            pass
        
        for r in self.arene.robot:

            tag_robot = "robot_" + str(self.arene.robot.index(r))
            self.arene_canvas.create_polygon(r.points, fill = "yellow", tags = tag_robot)
            self.arene_canvas.create_text(r.center[0], r.center[1], text = self.arene.robot.index(r) + 1, \
                fill = "black", tags = tag_robot)
            self.arene_canvas.create_line(r.center[0] + r.longueur // 2, r.center[1], r.center[0] + r.longueur, \
                r.center[1], tags = tag_robot)
            self.arene_canvas.create_line(r.center[0] + r.longueur, r.center[1], r.center[0] + r.longueur \
                - 10, r.center[1] - 10, tags = tag_robot)
            self.arene_canvas.create_line(r.center[0] + r.longueur, r.center[1], r.center[0] + r.longueur \
                - 10, r.center[1] + 10, tags = tag_robot)

    def creerObjet(self):
        pass

    def creerRobot(self):   
        
        def ok_button():
            fen.destroy()
            r = Robot(posx.get(), posy.get(), posz.get())
            self.arene.robot.append(r)

            tag_robot = "robot_" + str(self.arene.robot.index(r))
            print(tag_robot)
            self.arene_canvas.create_polygon(r.points, fill = "yellow", tags = tag_robot)
            self.arene_canvas.create_text(r.center[0], r.center[1], text = self.arene.robot.index(r) + 1, \
                fill = "black", tags = tag_robot)
            self.arene_canvas.create_line(r.center[0] + r.longueur // 2, r.center[1], r.center[0] + r.longueur, \
                r.center[1], tags = tag_robot)
            self.arene_canvas.create_line(r.center[0] + r.longueur, r.center[1], r.center[0] + r.longueur \
                - 10, r.center[1] - 10, tags = tag_robot)
            self.arene_canvas.create_line(r.center[0] + r.longueur, r.center[1], r.center[0] + r.longueur \
                - 10, r.center[1] + 10, tags = tag_robot)

        fen = Toplevel(self.fenetre)
        fen.title("Ajouter robot")
        fen.resizable(0, 0)

        posx = IntVar()
        posy = IntVar()
        posz = IntVar()

        Label(fen, text = "x =").grid(row = 0, column = 0)
        Label(fen, text = "y =").grid(row = 0, column = 2)
        Label(fen, text = "z =").grid(row = 0, column = 4)

        Entry(fen, textvariable = posx, width = 3).grid(row = 0, column = 1)
        Entry(fen, textvariable = posy, width = 3).grid(row = 0, column = 3)
        Entry(fen, textvariable = posz, width = 3).grid(row = 0, column = 5)

        ok = Button(fen, text = "Ok", command = ok_button)
        annuler = Button(fen, text = "Exit", command = fen.destroy)
        ok.grid(row = 3, column = 2)
        annuler.grid(row = 3,column = 3)

    def deplacerRobot(self):

        def ok_button():
            fen.destroy()

            for j in range(pas.get()):
                self.arene.robot[id_robot.get() - 1].avancer(x.get(), 0)
                #rob = self.arene.robot[id_robot.get() - 1]
                tag_robot = "robot_" + str(id_robot.get() - 1)
                self.arene_canvas.move(tag_robot, x.get(), 0)
                self.arene_canvas.update()
                time.sleep(.01)

        fen = Toplevel(self.fenetre)
        fen.title("Déplacer robot")
        fen.resizable(0, 0)

        id_robot = IntVar()
        x = DoubleVar()
        pas = IntVar()

        Label(fen, text = "id robot :").grid(row = 0, column = 0)
        Label(fen, text = "X :").grid(row = 0, column = 2)
        Label(fen, text = "pas :").grid(row = 0, column = 4)

        Entry(fen, textvariable = id_robot, width = 3).grid(row = 0, column = 1)
        Entry(fen, textvariable = x, width = 3).grid(row = 0, column = 3)
        Entry(fen, textvariable = pas, width = 3).grid(row = 0, column = 5)

        ok = Button(fen, text = "Ok", command = ok_button)
        annuler = Button(fen, text = "Exit", command = fen.destroy)
        ok.grid(row = 3, column = 2)
        annuler.grid(row = 3,column = 3)

    def tournerRobot(self):
        pass

arene = Terrain()
arene.objet.append(ObjetPhysique(50, 40, 0, 40, 10))
arene.objet.append(ObjetPhysique(400, 360, 0, 50, 30))
arene.objet.append(ObjetPhysique(780, 250, 0, 30, 30))
arene.robot.append(Robot(500, 200, 0))
fenetre = Fenetre_test(arene)

