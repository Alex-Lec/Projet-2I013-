#!/usr/bin/env python3
# -*- coding: utf-8 -*

from Terrain import *
from tkinter import *
from Robot import *
import time
#http://effbot.org/zone/tkinter-complex-canvas.htm
#http://www.fil.univ-lille1.fr/~marvie/python/chapitre6.html

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
        menu0.add_command(label = "Quitter", command = self.fenetre.destroy)
        menubar.add_cascade(label = "Fichier", menu = menu0)

        menu1 = Menu(menubar, tearoff = 0)
        menu1.add_command(label = "Créer robot", command = self.creerRobot)
        menu1.add_command(label = "Créer objet", command = self.creerObjet)
        menubar.add_cascade(label = "Création", menu = menu1)

        menu2 = Menu(menubar, tearoff = 0)
        menu2.add_command(label="Tourner robot", command = self.tournerRobot)
        menu2.add_command(label = "Déplacer robot", command = self.deplacerRobot)
        menubar.add_cascade(label = "Déplacement", menu = menu2)

        self.fenetre.config(menu = menubar)

        self.arene_canvas = Canvas(self.fenetre, width = 1000, height = 600)
        self.arene_canvas.pack()
        self.initialise_arene()
        self.fenetre.mainloop()

    def initialise_arene(self):

        for i in self.arene.objet:
            obj = self.arene_canvas.create_rectangle(i.x - i.largeur // 2, i.y - i.longueur // 2, \
                i.x + i.largeur // 2, i.y + i.longueur // 2, fill = "blue")
            self.listObjets += [obj]


        for i in self.arene.robot: #tous les objets de terrain sont transformés en forme

            rob = self.arene_canvas.create_polygon(i.points, fill="red",tag="polygon")
            self.arene_canvas.create_text(i.x, i.y, text = self.arene.robot.index(i), fill = "black")
            self.listRobots += [rob]

    def affichage_arene(self):

        self.arene_canvas.addtag_enclosed('del_items', 0, 0, 1000, 600)
        self.arene_canvas.delete('del_items')

        for i in self.arene.objet:
            self.arene_canvas.create_rectangle(i.x - i.largeur // 2, i.y - i.longueur // 2, \
                i.x + i.largeur // 2, i.y + i.longueur // 2, fill = "blue")

        for i in self.arene.robot: #tous les objets de terrain sont transformés en forme

            self.arene_canvas.create_polygon(i.points, fill="red")

            self.arene_canvas.create_text(i.x, i.y, text = self.arene.robot.index(i), fill = "black")

    def creerObjet(self):

        def ok_button():
            obj = self.arene.objet.append(ObjetPhysique(posx.get(), posy.get(), posz.get(), \
            largeur.get(),longueur.get(), hauteur.get()))

            self.listObjets += [obj]
            self.affichage_arene()
            fen.destroy()

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
            i = Robot(posx.get(), posy.get(), posz.get())
            self.arene.robot.append(i)

            points =   [ [posx + i.largeur//2 , posy +i.longueur//2 ],
            [posx + i.largeur//2, posy - i.longueur // 2],
            [posx - i.largeur//2, posy - i.longueur//2],
            [posx - i.largeur//2, posy + i.longueur//2]]
            rob = self.arene_canvas.create_polygon(points, fill="red")

            self.listRobots += [rob]
            self.affichage_arene()
            fen.destroy()

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
                rob = self.arene.robot[id_robot.get()]
                rob.avancer()
                x = rob.vecteur_direction.x
                y = rob.vecteur_direction.y
                self.affichage_arene()
                #self.arene_canvas.move(self.listRobots[id_robot.get()],x,y)
                self.arene_canvas.update()
                time.sleep(tps.get())


        fen = Toplevel(self.fenetre)
        fen.title("Déplacer robot")
        fen.resizable(0, 0)

        id_robot = IntVar()
        tps = DoubleVar()
        pas = IntVar()

        Label(fen, text = "id robot :").grid(row = 0, column = 0)
        Label(fen, text = "Temps :").grid(row = 0, column = 2)
        Label(fen, text = "pas :").grid(row = 0, column = 4)

        Entry(fen, textvariable = id_robot, width = 3).grid(row = 0, column = 1)
        Entry(fen, textvariable = tps, width = 3).grid(row = 0, column = 3)
        Entry(fen, textvariable = pas, width = 3).grid(row = 0, column = 5)

        ok = Button(fen, text = "Ok", command = ok_button)
        annuler = Button(fen, text = "Exit", command = fen.destroy)
        ok.grid(row = 3, column = 2)
        annuler.grid(row = 3,column = 3)



    def tournerRobot(self):

        def ok_button():
            fen.destroy()
            for j in range(angle.get()):
                rob = self.arene.robot[id_robot.get()]
                rob.tourner()
                
                self.arene_canvas.update()
                #time.sleep(.01)
                self.affichage_arene()


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
