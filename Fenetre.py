#!/usr/bin/env python3
# -*- coding: utf-8 -*
from Terrain import *
from tkinter import *



class Fenetre():


    def __init__(self, arenevirtuel=None):
        self.fenetre = Tk()
        self.fenetre.title("Simulateur")
        self.fenetre.geometry("1000x600")
        self.fenetre.resizable(0, 0)
        self.arenevirtuel = arenevirtuel
        
        self.robot = []
        self.obstacle = []
        #if (arenevirtuel == None):
        #    self.arenevirtuel = Terrain(1000,600)
        
        menubar = Menu(self.fenetre)
        menu1 = Menu(menubar, tearoff = 0)
        menu1.add_command(label = "Créer robot",command = lambda: creerRobot(self))
        menu1.add_command(label = "Créer objet",command = lambda: creerObjet(self))
        menu1.add_separator()
        menu1.add_command(label = "Quitter", command = self.fenetre.destroy)
        menubar.add_cascade(label = "Fichier", menu = menu1)
        menubar.add_cascade(label = "Options")
        
        self.fenetre.config(menu = menubar)
        self.arene = Canvas(self.fenetre, width = 1000, height = 600)
        self.arene.pack()
        
        for i in arenevirtuel.objet:
            if type(i).__name__ == 'Robot' :
                self.robot.append(self.arene.create_rectangle(i.x , i.y ,i.x + i.vdim.x, i.y + i.vdim.y, fill="red")
            else :
                self.robot.append(self.arene.create_rectangle(i.x , i.y ,i.x + i.vdim.x, i.y + i.vdim.y, fill="blue"))
        self.fenetre.mainloop()


    def actu_affichage(self):
        for i in self.arenevirtuel.objet:
            if type(i).__name__ == 'Robot' :
                self.arene.create_rectangle(i.x , i.y ,i.x + i.vdim.x, i.y + i.vdim.y, fill = "red")
            else :
                self.arene.create_rectangle(i.x , i.y ,i.x + i.vdim.x, i.y + i.vdim.y, fill = "blue")


    #@staticmethod
    def creerObjet(self):
    
        def creerObjectTerrain():
            vect = Vecteur(dimx.get(),dimy.get(),dimz.get())
            self.arenevirtuel.ajouter_objets([ObjetPhysique(posx.get(),posy.get(),posz.get(),vect)])
            #self.actu_affichage()
            fen.destroy()


        fen = Tk()
        fen.title("Ajouter object")

        Label(fen, text="x=").grid(row=0, column=0) #Utilisation d''un tableau pour gérer l'espace
        Label(fen, text="y=").grid(row=0, column=2)
        Label(fen, text="z=").grid(row=0, column=4)
        Label(fen, text="vx=").grid(row=1, column=0)
        Label(fen, text="vy=").grid(row=1, column=2)
        Label(fen, text="vz=").grid(row=1, column=4)
        
        posx = DoubleVar()
        posy = DoubleVar()
        posz = DoubleVar()
        dimx = DoubleVar()
        dimy = DoubleVar()
        dimz = DoubleVar()
        
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
    
        def creerRobotTerrain():
            vect = Vecteur(dimx.get(),dimy.get(),dimz.get())
            self.arenevirtuel.ajouter_objets([Robot(posx.get(),posy.get(),posz.get(),vect)])
            #self.actu_affichage()
            fen.destroy()
            
        fen = Tk()
        fen.title("Ajouter robot")

        Label(fen, text="x=").grid(row=0, column=0) #Utilisation d''un tableau pour gérer l'espace
        Label(fen, text="y=").grid(row=0, column=2)
        Label(fen, text="z=").grid(row=0, column=4)
        Label(fen, text="vx=").grid(row=1, column=0)
        Label(fen, text="vy=").grid(row=1, column=2)
        Label(fen, text="vz=").grid(row=1, column=4)
    
        posx = DoubleVar()
        posy = DoubleVar()
        posz = DoubleVar()
        dimx = DoubleVar()
        dimy = DoubleVar()
        dimz = DoubleVar()
    
        Entry(fen,textvariable = posx, width = 3).grid(row=0, column=1)
        Entry(fen,textvariable = posy, width = 3).grid(row=0, column=3)
        Entry(fen,textvariable = posz, width = 3).grid(row=0, column=5)
        Entry(fen,textvariable = dimx, width = 3).grid(row=1, column=1)
        Entry(fen,textvariable = dimy, width = 3).grid(row=1, column=3)
        Entry(fen,textvariable = dimz, width = 3).grid(row=1, column=5)
    
        ok = Button(fen, text = "Ok",command = creerRobotTerrain)
        annuler = Button(fen,text ="Exit",command = fen.destroy)
        
        ok.grid(row = 3, column=2)
        annuler.grid(row=3,column = 3)
        
        fen.mainloop()


