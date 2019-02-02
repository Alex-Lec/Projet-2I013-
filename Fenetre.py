#!/usr/bin/env python3
# -*- coding: utf-8 -*

from tkinter import *

class Fenetre():
    
    def __init__(self):

        self.fenetre = Tk()
        self.fenetre.title("Simulateur")
        self.fenetre.geometry("1000x600")
        self.fenetre.resizable(0, 0)
        menubar = Menu(self.fenetre)
        menu1 = Menu(menubar, tearoff = 0)
        menu1.add_command(label = "Créer robot")
        menu1.add_command(label = "Créer objet")
        menu1.add_separator()
        menu1.add_command(label = "Quitter", command = self.fenetre.destroy)
        menubar.add_cascade(label = "Fichier", menu = menu1)
        menubar.add_cascade(label = "Options")
        self.fenetre.config(menu = menubar)
        arene = Canvas(self.fenetre, width = 1000, height = 600)
        arene.pack()
        self.fenetre.mainloop()

"""Test Classe : 
fenetre = Fenetre()"""