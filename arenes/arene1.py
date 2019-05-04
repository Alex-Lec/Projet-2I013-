from composant import Rectangle
from code import Terrain

arene = Terrain()
arene.objet.append(Rectangle(700, 100, 100, 100, 100, 2))#plateau

arene.objet.append(Rectangle(655, 145, 0, 10, 10, 99))#jambe avant gauche
arene.objet.append(Rectangle(745, 145, 0, 10, 10, 99))#jambe avant droite

arene.objet.append(Rectangle(655, 55, 0, 10, 10, 99))#jambe arrières gauche
arene.objet.append(Rectangle(745, 55, 0, 10, 10, 99))#jambe arrières droite

arene.objet.append(Rectangle(700, 55, 100, 10, 100, 99))#dossier

arene.objet.append(Rectangle(700, 300, 100, 100, 100, 2))#plateau
arene.objet.append(Rectangle(655, 345, 0, 10, 10, 99))#jambe avant gauche
arene.objet.append(Rectangle(745, 345, 0, 10, 10, 99))#jambe avant droite

arene.objet.append(Rectangle(655, 255, 0, 10, 10, 99))#jambe arrières gauche
arene.objet.append(Rectangle(745, 255, 0, 10, 10, 99))#jambe arrières droite



arene.objet.append(Rectangle(700, 500, 100, 100, 100, 2))#plateau
    
arene.objet.append(Rectangle(655, 545, 0, 10, 10, 99))#jambe avant gauche
arene.objet.append(Rectangle(745, 545, 0, 10, 10, 99))#jambe avant droite

arene.objet.append(Rectangle(655, 455, 0, 10, 10, 99))#jambe arrières gauche
arene.objet.append(Rectangle(745, 455, 0, 10, 10, 99))#jambe arrières droite
arene.objet.append(Rectangle(700, 545, 100, 10, 100, 99))#dossier

arene.sauvegarder_arene("arene1")
