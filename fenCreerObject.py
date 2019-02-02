from tkinter import *

def creerObject():
    fen = Tk()
    fen.title("Ajouter object")

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
    
    ok = Button(fen, text = "Ok",command= lambda: creerObjTerrain(fen))
    annuler = Button(fen,text ="Exit",command = fen.destroy)
    ok.grid(row = 3, column=2)
    annuler.grid(row=3,column = 3)
    fen.mainloop()
    
def creerObjTerrain(root):
    #vect = Vecteur(dimx.get(),dimy.get(),dimz.get())
    #terrain.ajouter_objet(ObjectPhysique(posx.get(),posy.get(),posz.get(),vect))
    root.destroy()
    
