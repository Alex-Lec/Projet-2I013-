#!/usr/bin/env python3
# -- coding: utf-8 -

from .terrain import Terrain
from composant import Robot, Rectangle
from diver import *
import time
from threading import Thread
import sys

class Affichage(Thread):

    def __init__(self, arene = Terrain()):

        super(Affichage, self).__init__()
        self.arene = arene
        self.tps = 25

    def init_run(self):

        """
        Création de la fenêtre avec ses différents menus
        """

        self.fenetre = Tk()
        self.fenetre.title("Simulateur")
        self.fenetre.geometry("1500x900")
        self.fenetre.resizable(0, 0)
        self.robot_selectionne = IntVar()

        menubar = Menu(self.fenetre)

        menu0 = Menu(menubar, tearoff= 0)
        menu0.add_command(label = "Ouvrir", command = self.ouvrir)
        menu0.add_command(label = "Enregistrer", command = self.enregistrer)
        menu0.add_separator()
        menu0.add_command(label = "Quitter", command = self.fenetre.destroy)
        menubar.add_cascade(label = "Fichier", menu = menu0)

        menu1 = Menu(menubar, tearoff = 0)
        menu1.add_command(label = "Créer robot", command = self.creerRobot)
        menu1.add_command(label = "Créer objet", command = self.creerObjet)
        menubar.add_cascade(label = "Création", menu = menu1)
        
        self.canvas = Canvas(self.fenetre, width = 2000, height = 1000)
        self.canvas.pack()
        self.update_robots()
        self.update_objets()
        
    def run(self):
        self.init_run()
        self.fenetre.after(int(1000./self.tps),self.update_robots)
        self.fenetre.mainloop()

    def select_robot(self):
        print(self.robot_selectionne.get())

    def update_objets(self):

        """
        Met à jour le positionnement des objets dans l'arène
        Efface l'ancienne représentation des objets et en recréer une nouvelle
        """

        for o in self.arene.objet:
            if (self.arene.objet.index(o) > 3):
                tag_objet = "objet_" + str(self.arene.objet.index(o))
                self.canvas.delete(tag_objet)
                
                self.canvas.create_polygon(o.get_points(), fill = "blue", tags = tag_objet)
                self.canvas.create_text(o.x, o.y, text = self.arene.objet.index(o) - 3, \
                    fill = "black", tags = tag_objet)
        
    def update_robots(self):

        """
        Met à jour le positionnement des robots dans l'arène
        Efface l'ancienne représentation des robots et en recréer une nouvelle
        """

        for r in self.arene.robot:
            tag_robot = "robot_" + str(self.arene.robot.index(r))
            self.canvas.delete(tag_robot)
            
            self.canvas.create_polygon(r.get_points(), fill = "red", tags = tag_robot)
            self.canvas.create_text(r.x, r.y, text = self.arene.robot.index(r) + 1, \
                                    fill = "black", tags = tag_robot)

            self.canvas.create_line(r.x + r.v_dir.x * 20, r.y + \
                                    r.v_dir.y * 20, r.x + r.v_dir.x * 40, r.y + \
                                    r.v_dir.y * 40, fill = "black", tags = tag_robot)
        #self.fenetre.after(int(1000./self.tps),self.update_robots)
        self.fenetre.after(5,self.update_robots)
        
    def ouvrir(self):

        """
        Charge une arène à partir d'un fichier
        Appelle la fonction ouvri_arene de la classe Terrain
        """

        def ok_button():
            fen.destroy()
            self.arene.ouvrir_arene(nom_fichier.get())
            self.canvas.addtag_enclosed("del", 0, 0,2000, 1000)
            self.canvas.delete("del")
        
        fen = Toplevel(self.fenetre)
        fen.resizable(0, 0)
        fen.title("Ouvrir une sauvegarde")

        nom_fichier = StringVar()

        Label(fen, text="Nom du fichier (sans extension) =").grid(row = 0, column = 0)
        Entry(fen,textvariable = nom_fichier).grid(row = 0, column = 1)

        ok = Button(fen, text = "Ok",command = ok_button)
        ok.grid(row = 1, column = 0)
        annuler = Button(fen,text ="Exit",command = fen.destroy)
        annuler.grid(row = 1, column = 1)

    def enregistrer(self):

        """
        Sauvegarde une arène dans un fichier
        Appelle la fonction sauvergarder_arene de la classe Terrain
        """

        def ok_button():
            fen.destroy()
            self.arene.sauvegarder_arene(nom_fichier.get())

        fen = Toplevel(self.fenetre)
        fen.resizable(0, 0)
        fen.title("Ouvrir une sauvegarde")

        nom_fichier = StringVar()

        Label(fen, text="Nom du fichier (sans extension) =").grid(row = 0, column = 0)
        Entry(fen,textvariable = nom_fichier).grid(row = 0, column = 1)

        ok = Button(fen, text = "Ok",command = ok_button)
        ok.grid(row = 1, column = 0)
        annuler = Button(fen,text ="Exit",command = fen.destroy)
        annuler.grid(row = 1, column = 1)


    def creerObjet(self):

        """
        Créer un objet dans l'arène
        """

        def ok_button():

            fen.destroy()
            obj = Rectangle(posx.get(), posy.get(), posz.get(), 
                                largeur.get(),longueur.get(), hauteur.get())
                                
            self.arene.objet.append(obj)
            self.update_objets()

        fen = Toplevel(self.fenetre)
        fen.title("Ajouter objet")

        posx = IntVar()
        posy = IntVar()
        posz = IntVar()
        largeur = IntVar()
        longueur = IntVar()
        hauteur = IntVar()

        Label(fen, text="x =").grid(row = 0, column = 0)
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

        """
        Créer un robot dans l'arène
        """
        
        def ok_button():
            fen.destroy()
            r = Robot(posx.get(), posy.get(), posz.get())
            self.arene.robot.append(r)
            
            self.update_robots()

            self.menu3.add_separator()
            self.menu3.add_radiobutton(label = len(self.arene.robot), 
                            variable = self.robot_selectionne, \
                value = len(self.arene.robot), command = self.select_robot)

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
        
        


