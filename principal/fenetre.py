#!/usr/bin/env python3
# -- coding: utf-8 -

from .terrain import Terrain
from composant import Robot, ObjetPhysique
from diver import *
import time

# http://effbot.org/zone/tkinter-complex-canvas.htm
# http://www.fil.univ-lille1.fr/~marvie/python/chapitre6.html

class Fenetre():

    def __init__(self, arene = Terrain()):
        
        self.fenetre = Tk()
        self.fenetre.title("Simulateur")
        self.fenetre.geometry("1000x600")
        self.fenetre.resizable(0, 0)
        self.arene = arene
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

        menu2 = Menu(menubar, tearoff = 0)
        menu2.add_command(label="Tourner robot", command = self.tournerRobot)
        menu2.add_command(label = "Déplacer robot", command = self.deplacerRobot)
        menubar.add_cascade(label = "Déplacement", menu = menu2)

        self.menu3 = Menu(menubar, tearoff = 0)

        for i in range(1, len(self.arene.robot) + 1):
            self.menu3.add_radiobutton(label = i, variable = self.robot_selectionne, value = i, command = self.select_robot)

            if (i != 1):
                self.menu3.add_separator()

        menubar.add_cascade(label = "Sélectionner robot", menu = self.menu3)

        self.fenetre.config(menu = menubar)

        self.arene_canvas = Canvas(self.fenetre, width = 1000, height = 600)
        self.fenetre.bind("<Key>", self.deplacement)
        self.arene_canvas.pack()
        self.initialise_arene()
        self.fenetre.mainloop()

    def deplacement(self, event):

        if (event.keycode == 111 and self.robot_selectionne.get() != 0): #UP

            tag_robot = "robot_" + str(self.robot_selectionne.get() - 1)

            r = self.arene.robot[self.robot_selectionne.get() - 1]        

            self.arene.avancer_robot(r)

            self.arene_canvas.delete(tag_robot)
            self.arene_canvas.update()

            self.arene_canvas.create_polygon(r.points, fill = "red", tags = tag_robot)
            self.arene_canvas.create_text(r.x, r.y, text = self.arene.robot.index(r) + 1, \
                fill = "black", tags = tag_robot)

            self.arene_canvas.create_line(r.x + r.vecteur_direction.x * 20, r.y + \
                r.vecteur_direction.y * 20, r.x + r.vecteur_direction.x * 40, r.y + \
                    r.vecteur_direction.y * 40, fill = "black", tags = tag_robot)

            self.arene_canvas.update()

        elif (event.keycode == 116 and self.robot_selectionne.get() != 0): #DOWN

            tag_robot = "robot_" + str(self.robot_selectionne.get() - 1)

            r = self.arene.robot[self.robot_selectionne.get() - 1]        

            self.arene.reculer_robot(r)

            self.arene_canvas.delete(tag_robot)
            self.arene_canvas.update()

            self.arene_canvas.create_polygon(r.points, fill = "red", tags = tag_robot)
            self.arene_canvas.create_text(r.x, r.y, text = self.arene.robot.index(r) + 1, \
                fill = "black", tags = tag_robot)

            self.arene_canvas.create_line(r.x + r.vecteur_direction.x * 20, r.y + \
                r.vecteur_direction.y * 20, r.x + r.vecteur_direction.x * 40, r.y + \
                    r.vecteur_direction.y * 40, fill = "black", tags = tag_robot)

            self.arene_canvas.update()

        elif (event.keycode == 114 and self.robot_selectionne.get() != 0): #RIGHT

            r = self.arene.robot[self.robot_selectionne.get() - 1]
            
            self.arene.tourner_robot_d(r)

            tag_robot = "robot_" + str(self.robot_selectionne.get() - 1)

            self.arene_canvas.delete(tag_robot)
            self.arene_canvas.update()

            self.arene_canvas.create_polygon(r.points, fill = "red", tags = tag_robot)
            self.arene_canvas.create_text(r.x, r.y, text = self.arene.robot.index(r) + 1, \
                fill = "black", tags = tag_robot)

            self.arene_canvas.create_line(r.x + r.vecteur_direction.x * 20, r.y + \
                r.vecteur_direction.y * 20, r.x + r.vecteur_direction.x * 40, r.y + \
                    r.vecteur_direction.y * 40, fill = "black", tags = tag_robot)

            self.arene_canvas.update()

        elif (event.keycode == 113 and self.robot_selectionne.get() != 0): #LEFT

            r = self.arene.robot[self.robot_selectionne.get() - 1]
            
            self.arene.tourner_robot_g(r)

            tag_robot = "robot_" + str(self.robot_selectionne.get() - 1)

            self.arene_canvas.delete(tag_robot)
            self.arene_canvas.update()

            self.arene_canvas.create_polygon(r.points, fill = "red", tags = tag_robot)
            self.arene_canvas.create_text(r.x, r.y, text = self.arene.robot.index(r) + 1, \
                fill = "black", tags = tag_robot)

            self.arene_canvas.create_line(r.x + r.vecteur_direction.x * 20, r.y + \
                r.vecteur_direction.y * 20, r.x + r.vecteur_direction.x * 40, r.y + \
                    r.vecteur_direction.y * 40, fill = "black", tags = tag_robot)

            self.arene_canvas.update()

    def select_robot(self):
        print(self.robot_selectionne.get())

    def ouvrir(self):

        def ok_button():
            fen.destroy()
            self.arene.ouvrir_arene(nom_fichier.get())
            self.arene_canvas.addtag_enclosed("del", 0, 0, 1000, 600)
            self.arene_canvas.delete("del")
            self.initialise_arene()
        
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

    def initialise_arene(self):

        for o in self.arene.objet:
            
            if (self.arene.objet.index(o) > 3):

                tag_objet = "objet_" + str(self.arene.objet.index(o))
                self.arene_canvas.create_polygon(o.points, fill = "blue", tags = tag_objet)
                self.arene_canvas.create_text(o.x, o.y, text = self.arene.objet.index(o) - 3, \
                    fill = "black", tags = tag_objet)
        
        for r in self.arene.robot:

            tag_robot = "robot_" + str(self.arene.robot.index(r))
            self.arene_canvas.create_polygon(r.points, fill = "red", tags = tag_robot)
            self.arene_canvas.create_text(r.x, r.y, text = self.arene.robot.index(r) + 1, \
                fill = "black", tags = tag_robot)

            self.arene_canvas.create_line(r.x + r.vecteur_direction.x * 20, r.y + \
                    r.vecteur_direction.y * 20, r.x + r.vecteur_direction.x * 40, r.y + \
                        r.vecteur_direction.y * 40, fill = "black", tags = tag_robot)
                        
    def update_arene(self):
        for i in range(len(arene.robot)):
            tag_robot = "robot_" + str(i)

            self.arene_canvas.delete(tag_robot)

            self.arene_canvas.create_polygon(r.points, fill = "red", tags = tag_robot)
            
            self.arene_canvas.create_text(r.x, r.y, text = self.arene.robot.index(r) + 1, \
                fill = "black", tags = tag_robot)

            self.arene_canvas.create_line(r.x + r.vecteur_direction.x * 20, r.y + \
                r.vecteur_direction.y * 20, r.x + r.vecteur_direction.x * 40, r.y + \
                    r.vecteur_direction.y * 40, fill = "black", tags = tag_robot)

            self.arene_canvas.update()
    
    
    

    def creerObjet(self):

        def ok_button():

            fen.destroy()
            obj = ObjetPhysique(posx.get(), posy.get(), posz.get(), largeur.get(),longueur.get(), hauteur.get())
            self.arene.objet.append(obj)

            tag_objet = "objet_" + str(self.arene.objet.index(obj))
            self.arene_canvas.create_polygon(obj.points, fill = "blue", tags = tag_objet)
            self.arene_canvas.create_text(obj.x, obj.y, text = self.arene.objet.index(obj) - 3, \
                fill = "black", tags = tag_objet)

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
        
        def ok_button():
            fen.destroy()
            r = Robot(posx.get(), posy.get(), posz.get())
            self.arene.robot.append(r)

            tag_robot = "robot_" + str(self.arene.robot.index(r))
            self.arene_canvas.create_polygon(r.points, fill = "red", tags = tag_robot)
            self.arene_canvas.create_text(r.x, r.y, text = self.arene.robot.index(r) + 1, \
                fill = "black", tags = tag_robot)

            self.arene_canvas.create_line(r.x + r.vecteur_direction.x * 20, r.y + \
                    r.vecteur_direction.y * 20, r.x + r.vecteur_direction.x * 40, r.y + \
                        r.vecteur_direction.y * 40, fill = "black", tags = tag_robot)

            self.menu3.add_separator()
            self.menu3.add_radiobutton(label = len(self.arene.robot), variable = self.robot_selectionne, \
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

    def deplacerRobot(self):

        def ok_button():

            fen.destroy()
            tag_robot = "robot_" + str(id_robot.get() - 1)

            r = self.arene.robot[id_robot.get() - 1]

            for j in range(abs(pas.get())):
                if (pas.get() < 0):
                    self.arene.reculer_robot(r)
                else :
                    self.arene.avancer_robot(r)
                
                tag_robot = "robot_" + str(id_robot.get() - 1)

                self.arene_canvas.delete(tag_robot)

                self.arene_canvas.create_polygon(r.points, fill = "red", tags = tag_robot)
                
                self.arene_canvas.create_text(r.x, r.y, text = self.arene.robot.index(r) + 1, \
                    fill = "black", tags = tag_robot)

                self.arene_canvas.create_line(r.x + r.vecteur_direction.x * 20, r.y + \
                    r.vecteur_direction.y * 20, r.x + r.vecteur_direction.x * 40, r.y + \
                        r.vecteur_direction.y * 40, fill = "black", tags = tag_robot)

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
            r = self.arene.robot[id_robot.get() - 1]

            
            for j in range(abs(angle.get())):
                if (angle.get() < 0):
                    self.arene.tourner_robot_d(r)
                else :
                    self.arene.tourner_robot_g(r)

                tag_robot = "robot_" + str(id_robot.get() - 1)

                self.arene_canvas.delete(tag_robot)

                self.arene_canvas.create_polygon(r.points, fill = "red", tags = tag_robot)
                
                self.arene_canvas.create_text(r.x, r.y, text = self.arene.robot.index(r) + 1, \
                    fill = "black", tags = tag_robot)

                self.arene_canvas.create_line(r.x + r.vecteur_direction.x * 20, r.y + \
                    r.vecteur_direction.y * 20, r.x + r.vecteur_direction.x * 40, r.y + \
                        r.vecteur_direction.y * 40, fill = "black", tags = tag_robot)

                self.arene_canvas.update()
                time.sleep(0.02)

        fen = Toplevel(self.fenetre)
        fen.title("Tourner robot")
        fen.resizable(0, 0)

        id_robot = IntVar()
        angle = IntVar()

        Label(fen, text = "id robot :").grid(row = 0, column = 0)
        Label(fen, text = "Angle° :").grid(row = 0, column = 2)

        Entry(fen, textvariable = id_robot, width = 3).grid(row = 0, column = 1)
        Entry(fen, textvariable = angle, width = 3).grid(row = 0, column = 3)

        ok = Button(fen, text = "Ok", command = ok_button)
        annuler = Button(fen, text = "Exit", command = fen.destroy)
        ok.grid(row = 3, column = 1)
        annuler.grid(row = 3,column = 2)
        
        
        """
        def clavier(self,event):
            global coords
            touche = event.keysym
            if touche == "Up":                
            elif touche == "Down":
            elif touche == "Right":
            elif touche == "Left":
            
        """
        
        
