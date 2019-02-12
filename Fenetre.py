#!/usr/bin/env python3
# -*- coding: utf-8 -*

from Terrain import *
from tkinter import *
from Robot import *
import time

# http://effbot.org/zone/tkinter-complex-canvas.htm
# http://www.fil.univ-lille1.fr/~marvie/python/chapitre6.html

class Fenetre():

    def __init__(self, arene = Terrain()):

        self.fenetre = Tk()
        self.fenetre.title("Simulateur")
        self.fenetre.geometry("1000x600")
        self.fenetre.resizable(0, 0)
        self.arene = arene
        self.listRobots = [] #Ne doit contenir que des rectangles canevas
        self.listObjets = [] #Ne doit contenir que des rectangles canevas

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

        self.initialise_arene()
        self.fenetre.mainloop()

    def initialise_arene(self):

        for o in self.arene.objet:

            obj_canvas = Canvas(self.fenetre)
            obj_canvas.create_rectangle(0, 0, o.largeur + 1, o.longueur + 1, fill = "blue")
            obj_canvas.place(x = o.x, y = o.y)
            self.listObjets.append(obj_canvas)

        for r in self.arene.robot:
            rob_canvas = Canvas(self.fenetre, bg = "purple")
            #rob_canvas.create_rectangle(0, 0, r.largeur + 1, r.longueur + 1, fill = "red")
            rob_canvas.create_polygon(r.points2, fill = "yellow" ,tags = "polygon" )
            rob_canvas.create_text(r.largeur // 2, r.longueur // 2, text = self.arene.robot.index(r) + 1, fill = "black")
            rob_canvas.create_line(r.largeur // 2 + r.largeur // 4, r.longueur // 2, r.largeur , r.longueur // 2)
            rob_canvas.create_line(r.largeur, r.longueur // 2, r.largeur - 10, r.longueur // 2 - 10)
            rob_canvas.create_line(r.largeur, r.longueur // 2, r.largeur - 10, r.longueur // 2 + 10)
            rob_canvas.place(x = r.x, y = r.y)
            self.listRobots.append(rob_canvas)

    def creerObjet(self):

        def ok_button():
            fen.destroy()
            obj = ObjetPhysique(posx.get(), posy.get(), posz.get(), largeur.get(),longueur.get(), hauteur.get())
            self.listObjets.append(obj)

            obj_canvas = Canvas(self.fenetre, width = obj.largeur, height = obj.longueur)
            obj_canvas.create_rectangle(0, 0, obj.largeur + 1, obj.longueur + 1, fill = "blue")
            obj_canvas.place(x = obj.x, y = obj.y)
            self.listObjets.append(obj_canvas)

        fen = Toplevel(self.fenetre)
        fen.title("Ajouter objet")

        posx = IntVar()
        posy = IntVar()
        posz = IntVar()
        largeur = IntVar()
        longueur = IntVar()
        hauteur = IntVar()

        Label(fen, text="x =").grid(row = 0, column = 0) #Utilisation d''un tableau pour gérer l'espace
        Label(fen, text="y =").grid(row = 0, column = 2)
        Label(fen, text="z =").grid(row = 0, column = 4)
        Label(fen, text="Largeur =").grid(row = 1, column = 0)
        Label(fen, text="Longueur =").grid(row = 1, column = 2)
        Label(fen, text="Hauteur =").grid(row = 1, column = 4)

        Entry(fen,textvariable = posx, width = 3).grid(row = 0, column = 1)
        Entry(fen,textvariable = posy, width = 3).grid(row = 0, column = 3)
        Entry(fen,textvariable = posz, width = 3).grid(row = 0, column = 5)
        Entry(fen,textvariable = largeur, width = 3).grid(row = 1, column = 1)
        Entry(fen,textvariable = longueur, width = 3).grid(row = 1, column = 3)
        Entry(fen,textvariable = hauteur, width = 3).grid(row = 1, column = 5)

        ok = Button(fen, text = "Ok",command = ok_button)
        ok.grid(row = 3, column = 2)
        annuler = Button(fen,text ="Exit",command = fen.destroy)
        annuler.grid(row = 3, column = 3)

    def creerRobot(self):

        def ok_button():
            fen.destroy()
            r = Robot(posx.get(), posy.get(), posz.get())
            self.arene.robot.append(r)

            points = [
                [posx.get() - r.largeur // 2, posy.get() - r.longueur // 2],
                [posx.get() + r.largeur // 2, posy.get() + r.longueur // 2],
                [posx.get() + r.largeur // 2, posy.get() - r.longueur // 2],
                [posx.get() - r.largeur // 2, posy.get() + r.longueur // 2]]

            rob_canvas = Canvas(self.fenetre, width = r.largeur, height = r.longueur)
            #rob_canvas.create_rectangle(0, 0, r.largeur + 1, r.longueur + 1, fill = "red")
            rob_canvas.create_polygon(points, fill = "red")
            rob_canvas.create_text(r.largeur // 2, r.longueur // 2, text = self.arene.robot.index(r) + 1, fill = "black")
            rob_canvas.create_line(r.largeur // 2 + r.largeur // 4, r.longueur // 2, r.largeur , r.longueur // 2)
            rob_canvas.create_line(r.largeur, r.longueur // 2, r.largeur - 10, r.longueur // 2 - 10)
            rob_canvas.create_line(r.largeur, r.longueur // 2, r.largeur - 10, r.longueur // 2 + 10)
            rob_canvas.place(x = r.x, y = r.y)
            self.listRobots.append(rob_canvas)

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
                rob = self.arene.robot[id_robot.get() - 1]
                self.listRobots[id_robot.get() - 1].place(x = rob.x, y = rob.y)
                self.listRobots[id_robot.get() - 1].update()
                self.fenetre.update()
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

        def ok_button():

            fen.destroy()

            self.arene.robot[id_robot.get() - 1].tourner(angle.get(), \
                self.arene.robot[id_robot.get() - 1].points, self.arene.robot[id_robot.get() - 1].center)

            rob = self.arene.robot[id_robot.get() - 1]
            #self.arene_canvas.move(self.listRobots[id_robot.get()],x.get(),0)
            #self.arene_canvas.update()

            #Déplace les quatre points
            self.listRobots[id_robot.get() - 1].delete("polygon")
            self.listRobots[id_robot.get() - 1].create_polygon(self.arene.robot[id_robot.get() - 1].points2, \
                fill = "red",tags = "polygon")

            self.listRobots[id_robot.get() - 1].place(x = rob.x, y = rob.y)

            self.listRobots[id_robot.get() - 1].update()
            self.fenetre.update()
            time.sleep(.01)

        fen = Toplevel(self.fenetre)
        fen.title("Tourner robot")
        fen.resizable(0, 0)

        id_robot = IntVar()
        angle = IntVar()

        Label(fen, text = "id robot :").grid(row = 0, column = 0)
        Label(fen, text = "Angle° :").grid(row = 0, column = 2)
        #Label(fen, text = "pas :").grid(row = 0, column = 4)

        Entry(fen, textvariable = id_robot, width = 3).grid(row = 0, column = 1)
        Entry(fen, textvariable = angle, width = 3).grid(row = 0, column = 3)
        #Entry(fen, textvariable = pas, width = 3).grid(row = 0, column = 5)

        ok = Button(fen, text = "Ok", command = ok_button)
        annuler = Button(fen, text = "Exit", command = fen.destroy)
        ok.grid(row = 3, column = 1)
        annuler.grid(row = 3,column = 2)
