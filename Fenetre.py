#!/usr/bin/env python3
# -*- coding: utf-8 -*

from Terrain import *
from tkinter import *

def creerObjTerrain(root):
    #vect = Vecteur(dimx.get(),dimy.get(),dimz.get())
    #terrain.ajouter_objet(ObjectPhysique(posx.get(),posy.get(),posz.get(),vect))
    root.destroy()
    
def creerRobotTerrain(root):
    #vect = Vecteur(dimx.get(),dimy.get(),dimz.get())
    #terrain.ajouter_objet(ObjectPhysique(posx.get(),posy.get(),posz.get(),vect))
    root.destroy()

class Fenetre():
    
    def __init__(self, arene_virtuelle = Terrain()):

        self.fenetre = Tk()
        self.fenetre.title("Simulateur")
        self.fenetre.geometry("1000x600")
        self.fenetre.resizable(0, 0)
        
        menubar = Menu(self.fenetre)
        menu1 = Menu(menubar, tearoff = 0)
        menu1.add_command(label = "Créer robot", command = lambda : self.creerObject())
        menu1.add_command(label = "Créer objet", command = lambda : self.creerRobot())
        menu1.add_separator()
        menu1.add_command(label = "Quitter", command = self.fenetre.destroy)
        menubar.add_cascade(label = "Fichier", menu = menu1)
        menubar.add_cascade(label = "Options")
        self.fenetre.config(menu = menubar)
        arene = Canvas(self.fenetre, width = 1000, height = 600)

        for i in arene_virtuelle.objet: #tous les objets de terrain sont transformés en forme
            arene.create_rectangle(i.x - i.largeur // 2, i.y - i.longueur // 2, \
                i.x + i.largeur // 2, i.y + i.longueur // 2, fill = "black")

        arene.pack()
            
        self.fenetre.mainloop()

    def creerObject(self):
        fen = Tk()
        fen.title("Ajouter object")

        l1 = Label(fen, text="x=").grid(row=0, column=0) #Utilisation d''un tableau pour gérer l'espace
        l2 = Label(fen, text="y=").grid(row=0, column=2)
        l3 = Label(fen, text="z=").grid(row=0, column=4)
        l4 = Label(fen, text="vx=").grid(row=1, column=0)
        l5 = Label(fen, text="vy=").grid(row=1, column=2)
        l6 = Label(fen, text="vz=").grid(row=1, column=4)
    
        posx = Entry(fen,takefocus = 1,width = 3).grid(row=0, column=1)
        posy = Entry(fen, takefocus = 2, width = 3).grid(row=0, column=3)
        posz = Entry(fen, takefocus = 3, width = 3).grid(row=0, column=5)
    
        dimx = Entry(fen, width = 3).grid(row=1, column=1)
        dimy = Entry(fen, width = 3).grid(row=1, column=3)
        dimz = Entry(fen, width = 3).grid(row=1, column=5)
    
        ok = Button(fen, text = "Ok",command = lambda: creerObjTerrain(fen))
        annuler = Button(fen,text ="Exit",command = fen.destroy)
        
        ok.grid(row = 3, column=2)
        annuler.grid(row=3,column = 3)
        
        fen.mainloop()
    
    def creerRobot(self):
        fen = Tk()
        fen.title("Ajouter robot")

        l1 = Label(fen, text="x=").grid(row=0, column=0)
        l2 = Label(fen, text="y=").grid(row=0, column=2)
        l3 = Label(fen, text="z=").grid(row=0, column=4)
        l4 = Label(fen, text="vx=").grid(row=1, column=0)
        l5 = Label(fen, text="vy=").grid(row=1, column=2)
        l6 = Label(fen, text="vz=").grid(row=1, column=4)
    
        posx = Entry(fen,takefocus = 1,width = 3).grid(row=0, column=1)
        posy = Entry(fen, takefocus = 2, width = 3).grid(row=0, column=3)
        posz = Entry(fen, takefocus = 3, width = 3).grid(row=0, column=5)
    
        dimx = Entry(fen, width = 3).grid(row=1, column=1)
        dimy = Entry(fen, width = 3).grid(row=1, column=3)
        dimz = Entry(fen, width = 3).grid(row=1, column=5)
    
        ok = Button(fen, text = "Ok",command= lambda: creerRobotTerrain(fen))
        annuler = Button(fen,text ="Exit",command = fen.destroy)
        ok.grid(row = 3, column=2)
        annuler.grid(row=3,column = 3)
        fen.mainloop()

"""
Test rendu graphique arène :

arene_virtuelle = Terrain()
arene_virtuelle.objet.append(ObjetPhysique(50, 40, 0, 40, 10))
arene_virtuelle.objet.append(ObjetPhysique(400, 360, 0, 50, 30))
arene_virtuelle.objet.append(ObjetPhysique(780, 250, 0, 30, 30))
fenetre = Fenetre(arene_virtuelle)
"""