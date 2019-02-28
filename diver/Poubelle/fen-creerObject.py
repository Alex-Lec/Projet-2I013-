from tkinter import *

def envoyeObject(fen):
    fen.quit

def callback():
    if askyesno('Titre 1', 'Êtes-vous sûr de vouloir faire ça?'):
        showwarning('Titre 2', 'Tant pis...')
    else:
        showinfo('Titre 3', 'Vous avez peur!')
        showerror("Titre 4", "Aha")




def creerObject():
    fen = Tk()
    fen.title("Ajouter object")
    fen.geometry("300x500")
    posx = Entry(fen, x = "x =").pack()
    posy = Entry(fen, y = "y =").pack()
    posz = Entry(fen, z = "z =").pack()

    dimx = Entry(fen, dx = "dim x =").pack()
    dimy = Entry(fen, dy = "dim y =").pack()
    dimz = Entry(fen, dz = "dim z =").pack()
    Button(text='Action', command=callback).pack()

    ok = Button(fen, text = "Ok", command=fen.quit).pack()
    fen.mainloop()

    return posx,posy,posz,dimx,dimy,dimz
