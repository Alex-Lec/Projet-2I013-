#!/usr/bin/env python3
# -*- coding: utf-8 -*

from Terrain import *
from tkinter import *
from Robot import *

#http://www.fil.univ-lille1.fr/~marvie/python/chapitre6.html

class Fenetre():

    def __init__(self, arene = Terrain()):

        self.fenetre = Tk()
        self.fenetre.title("Simulateur")
        self.fenetre.geometry("1000x600")
        self.fenetre.resizable(0, 0)
        self.arene = arene

        menubar = Menu(self.fenetre)

        menu0 = Menu(menubar, tearoff= 0)
        menu0.add_command(label = "Quitter", command = self.fenetre.destroy)
        menubar.add_cascade(label = "Fichier", menu = menu0)

        menu1 = Menu(menubar, tearoff = 0)
        menu1.add_command(label = "Créer robot", command = self.creerRobot)
        menu1.add_command(label = "Créer objet", command = self.creerObjet)
        menubar.add_cascade(label = "Création", menu = menu1)

        menu2 = Menu(menubar, tearoff = 0)
        menu2.add_command(label = "Déplacer robot", command = self.deplacerRobot)
        menubar.add_cascade(label = "Déplacement", menu = menu2)
        
        self.fenetre.config(menu = menubar)

        self.arene_canvas = Canvas(self.fenetre, width = 1000, height = 600)
        self.arene_canvas.pack()
        self.affichage_arene()
        self.fenetre.mainloop()

    def affichage_arene(self):
        
        self.arene_canvas.addtag_enclosed('del_items', 0, 0, 1000, 600)
        self.arene_canvas.delete('del_items')
    
        for i in self.arene.objet:
            self.arene_canvas.create_rectangle(i.x - i.largeur // 2, i.y - i.longueur // 2, \
                i.x + i.largeur // 2, i.y + i.longueur // 2, fill = "black")

        for i in self.arene.robot: #tous les objets de terrain sont transformés en forme
            self.arene_canvas.create_rectangle(i.x - i.largeur // 2, i.y - i.longueur // 2, \
                i.x + i.largeur // 2, i.y + i.longueur // 2, fill = "yellow")

            #self.arene_canvas.create_line(i.x, i.y, i.x + i.largeur // 2, i.y, fill = "black")
            #self.arene_canvas.create_line(i.x, i.y - i.longueur // 2, i.x, i.y + i.longueur // 2, fill = "black")
            self.arene_canvas.create_text(i.x, i.y, text = self.arene.robot.index(i) + 1, fill = "black")

    def creerObjet(self):
    
        def ok_button():
            self.arene.objet.append(ObjetPhysique(posx.get(), posy.get(), posz.get(), largeur.get(), \
                longueur.get(), hauteur.get()))
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
        
        Entry(fen,textvariable = posx, width = 3).grid(row=0, column=1)
        Entry(fen,textvariable = posy, width = 3).grid(row=0, column=3)
        Entry(fen,textvariable = posz, width = 3).grid(row=0, column=5)
        Entry(fen,textvariable = largeur, width = 3).grid(row=1, column=1)
        Entry(fen,textvariable = longueur, width = 3).grid(row=1, column=3)
        Entry(fen,textvariable = hauteur, width = 3).grid(row=1, column=5)

        ok = Button(fen, text = "Ok",command = ok_button)
        ok.grid(row = 3, column = 2)
        annuler = Button(fen,text ="Exit",command = fen.destroy)
        annuler.grid(row = 3, column = 3)    

    def creerRobot(self):

        def ok_button():
            self.arene.robot.append(Robot(posx.get(), posy.get(), posz.get()))
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
            self.arene.robot[id_robot.get()].avancer(x.get(), y.get())
            self.affichage_arene()
            fen.destroy()

        fen = Toplevel(self.fenetre)
        fen.title("Déplacer robot")
        fen.resizable(0, 0)

        id_robot = IntVar()
        x = IntVar()
        y = IntVar()

        Label(fen, text = "id robot :").grid(row = 0, column = 0)
        Label(fen, text = "Déplacement en x :").grid(row = 0, column = 2)
        Label(fen, text = "Déplacement en y:").grid(row = 0, column = 4)

        Entry(fen, textvariable = id_robot, width = 3).grid(row = 0, column = 1)
        Entry(fen, textvariable = x, width = 3).grid(row = 0, column = 3)
        Entry(fen, textvariable = y, width = 3).grid(row = 0, column = 5)

        ok = Button(fen, text = "Ok", command = ok_button)
        annuler = Button(fen, text = "Exit", command = fen.destroy)
        ok.grid(row = 3, column = 2)
        annuler.grid(row = 3,column = 3)