from Fenetre import*
from Terrain import*
from ObjetPhysique import*
from Vecteur import*
from Robot import*

"""
Le but ici, est de constuire quelques objets simples, un robot et de les afficher

"""
v1 = Vecteur(200, 60, 30)
v2 = Vecteur(70, 350, 30)
v3 = Vecteur(100, 100, 30)
vrob = Vecteur(50,100,10)

ob1 = ObjetPhysique(20, 60, 0, v1)
ob2 = ObjetPhysique(900, 200, 0, v2)
ob3 = ObjetPhysique(600, 100, 0, v3)
ob4 = ObjetPhysique(230,500,0,v3)

robot = Robot(0, 300, 0, vrob)

arene = Terrain(1000,600)
arene.ajouter_objets([ob1,ob2,ob3,ob4,robot])
fenetre = Fenetre(arene)

for i in range(100):
    robot.avancer(0,1)
    fenetre.actu_affichage()


#fenetre.mainloop()
