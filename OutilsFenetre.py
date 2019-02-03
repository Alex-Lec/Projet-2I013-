from Terrain import *
from tkinter import *
from Fenetre import *


class OutilsFenetre():

    @staticmethod
    def creerObject(terrain):
    
        def creerObjectTerrain(self):
            print(posx.get())
        #vect = Vecteur(dimx.get(),dimy.get(),dimz.get())
        #terrain.ajouter_objets([ObjetPhysique(posx.get(),posy.get(),posz.get(),vect)])
        #self.actu_affichage()
        #fen.destroy()


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
        
        ok = Button(fen, text = "Ok",command = self.creerObjectTerrain).grid(row = 3, column=2)
        annuler = Button(fen,text ="Exit",command = fen.destroy).grid(row=3,column = 3)        
        fen.mainloop()
    
    @staticmethod
    def creerRobot():
    
        def creerRobotTerrain():
            print(posx.get())
            
            #vect = Vecteur(dimx.get(),dimy.get(),dimz.get())
            #self.arenevirtuel.ajouter_objets([Robot(posx.get(),posy.get(),posz.get(),vect)])
            #self.actu_affichage()
            #fen.destroy()
            
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

    
    
