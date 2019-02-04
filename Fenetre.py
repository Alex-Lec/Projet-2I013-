#!/usr/bin/env python3
# -*- coding: utf-8 -*

from Terrain import *
from tkinter import *
from Robot import *

def creerObjTerrain(root):
    #vect = Vecteur(dimx.get(),dimy.get(),dimz.get())
    #terrain.ajouter_objet(ObjectPhysique(posx.get(),posy.get(),posz.get(),vect))
    root.destroy()
    
def creerRobotTerrain(root):
    #vect = Vecteur(dimx.get(),dimy.get(),dimz.get())
    #terrain.ajouter_objet(ObjectPhysique(posx.get(),posy.get(),posz.get(),vect))
    root.destroy()

class Fenetre():
    
    def __init__(self, arene = Terrain()):

        self.fenetre = Tk()
        self.fenetre.title("Simulateur")
        self.fenetre.geometry("1000x600")
        self.fenetre.resizable(0, 0)
        self.arene = arene
        
        menubar = Menu(self.fenetre)
        menu1 = Menu(menubar, tearoff = 0)
        menu1.add_command(label = "Créer robot", command = lambda : self.creerRobot())
        menu1.add_command(label = "Créer objet", command = lambda : self.creerObjet())
        menu1.add_separator()
        menu1.add_command(label = "Quitter", command = self.fenetre.destroy)
        menubar.add_cascade(label = "Fichier", menu = menu1)
        menubar.add_cascade(label = "Options")
        
        self.fenetre.config(menu = menubar)

    def affichage_arene(self):

        self.arene_canvas = Canvas(self.fenetre, width = 1000, height = 600)

        for i in self.arene.objet:
            self.arene_canvas.create_rectangle(i.x - i.largeur // 2, i.y - i.longueur // 2, \
                i.x + i.largeur // 2, i.y + i.longueur // 2, fill = "blue")

        for i in self.arene.robot:
            self.arene_canvas.create_rectangle(i.x - i.largeur // 2, i.y - i.longueur // 2, \
                i.x + i.largeur // 2, i.y + i.longueur // 2, fill = "red")

        self.arene_canvas.pack()
        self.fenetre.mainloop()


    #@staticmethod
    def creerObjet(self):
    
        def ok_button():
            print(self.posx)
            print(self.posx.get())
            #self.arene.robot.append(Robot(posx, posy, posz))
            #fen.destroy()

        fen = Tk()
        fen.title("Ajouter object")

        l1 = Label(fen, text="x =").grid(row = 0, column = 0)
        l2 = Label(fen, text="y =").grid(row = 0, column = 2)
        l3 = Label(fen, text="z =").grid(row = 0, column = 4)
        l4 = Label(fen, text="vx =").grid(row = 1, column = 0)
        l5 = Label(fen, text="vy =").grid(row = 1, column = 2)
        l6 = Label(fen, text="vz =").grid(row = 1, column = 4)
    
        posx = Entry(fen,takefocus = 1,width = 3).grid(row=0, column=1)
        posy = Entry(fen, takefocus = 2, width = 3).grid(row=0, column=3)
        posz = Entry(fen, takefocus = 3, width = 3).grid(row=0, column=5)
        dimx = Entry(fen, width = 3).grid(row=1, column=1)
        dimy = Entry(fen, width = 3).grid(row=1, column=3)
        dimz = Entry(fen, width = 3).grid(row=1, column=5)
    
        ok = Button(fen, text = "Ok",command = ok_button())
        annuler = Button(fen,text ="Exit",command = fen.destroy)
        
        posx, posy, posz , dimx, dimy, dimz= DoubleVar()
        
        Entry(fen,textvariable = posx, width = 3).grid(row=0, column=1)
        Entry(fen,textvariable = posy, width = 3).grid(row=0, column=3)
        Entry(fen,textvariable = posz, width = 3).grid(row=0, column=5)
        Entry(fen,textvariable = dimx, width = 3).grid(row=1, column=1)
        Entry(fen,textvariable = dimy, width = 3).grid(row=1, column=3)
        Entry(fen,textvariable = dimz, width = 3).grid(row=1, column=5)
        
        ok = Button(fen, text = "Ok",command = creerObjectTerrain).grid(row = 3, column=2)
        annuler = Button(fen,text ="Exit",command = fen.destroy).grid(row=3,column = 3)        
        fen.mainloop()

    #@staticmethod
    def creerRobot(self):

        def ok_button():
            print(self.posx)
            print(self.posx.get())
            #self.arene.robot.append(Robot(posx, posy, posz))
            #fen.destroy()

        self.fen = Tk()
        self.fen.title("Ajouter robot")
        self.fen.resizable(0, 0)

        self.posx = IntVar()
        self.posy = IntVar()
        self.posz = IntVar()

        Label(self.fen, text = "x =").grid(row = 0, column = 0)
        Label(self.fen, text = "y =").grid(row = 0, column = 2)
        Label(self.fen, text = "z =").grid(row = 0, column = 4)

        Entry(self.fen, textvariable = self.posx, width = 3).grid(row = 0, column = 1)
        Entry(self.fen, textvariable = self.posy, width = 3).grid(row = 0, column = 3)
        Entry(self.fen, textvariable = self.posz, width = 3).grid(row = 0, column = 5)

        self.ok = Button(self.fen, text = "Ok", command = ok_button)
        self.annuler = Button(self.fen, text = "Exit", command = self.fen.destroy)
        
        self.ok.grid(row = 3, column = 2)
        self.annuler.grid(row = 3,column = 3)

        self.fen.mainloop()


"""
Test rendu graphique arène :

arene = Terrain()
arene.objet.append(ObjetPhysique(50, 40, 0, 40, 10))
arene.objet.append(ObjetPhysique(400, 360, 0, 50, 30))
arene.objet.append(ObjetPhysique(780, 250, 0, 30, 30))
arene.robot.append(ObjetPhysique(500, 200, 0, 30, 30))
fenetre = Fenetre(arene)
fenetre.affichage_arene()
"""

