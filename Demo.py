from Fenetre import*
from Terrain import*
from ObjetPhysique import*
from Vecteur import*
from Robot import*

"""
Le but ici, est de constuire quelques objets simples, un robot et de les afficher

"""
v1 = Vecteur(30, 20, 30)
v2 = Vecteur(20, 60, 30)
v3 = Vecteur(50, 20, 30)
vrob = Vecteur(10,20,10)

ob1 = ObjetPhysique(20, 60, 0, v1)
ob2 = ObjetPhysique(500, 200, 0, v2)
ob3 = ObjetPhysique(50, 100, 0, v3)

robot = Robot(10, 40, 0, vrob)

arene = Terrain(1000,600)
arene.ajouter_objets([ob1,ob2,ob3,robot])

#fenetre = Fenetre(arene)
#fenetre.mainloop()
