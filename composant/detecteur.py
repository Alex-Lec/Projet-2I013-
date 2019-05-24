from math import sqrt
from .rectangle import Rectangle

class Detecteur:
    
    def __init__(self, robot):
        self.robot = robot
        
    def detecte(self):
        """
        Mesure la distance entre le devant du robot et les objets devant.
        Retourne l'objet ou le robot le plus proche devant le robot.
        NE MARCHE QUE SI ROBOT A UNE robot.arene !!!
        Concidére que tous les objets sont des polynopmes
        """
    
        if (self.robot.arene == None):
            return
        
        obj = self.robot.arene.objet + self.robot.arene.robot
        
        def mmsigne(a,b): #Utilisé pour savoir si un objet est devant ou derriére le robot
            if (a<0 and b<0):
                return True
            if (a==0 and b==0):
                return True
            return (a>0 and b>0)
            
        mini = 1000000 # Valeur par défaut
        #On crée [p1:p2] un segment partant du centre du robot dans le sens de son vecteur
        #direction, d'une longueur de la moitié de celle du robot associé.
        p1 = (self.robot.x,self.robot.y)
        p2 = (self.robot.x + (self.robot.longueur /2)*self.robot.v_dir.x,
              self.robot.y + (self.robot.longueur /2)*self.robot.v_dir.y)
              
        # Si le segment n'est pas dans l'axe x, on trouve l'équation de la droite de 
        # type a1*x + b1 passant par le segment
        if (round(p1[0]-p2[0],12) != 0): 
            a1 = (p1[1] - p2[1]) /(p1[0]- p2[0])
            b1 = p1[1] - a1*p1[0]
        
        # Si le robot est dans l'axe x, on garde cette info dans a1
        else :
            a1 = None 
            b1 = p1[0]
            
        for o in obj: # On iter sur tous les objets de l'aréne
            if (o == self.robot): # Le robot ne doit pas se detecter lui même
                continue
            
            opt = o.get_points() # On transforme l'objet en liste de points
            
            for j in range(len(opt)): # On iter sur tous les points de l'objet
                #On transforme chaques pt en segment avec le pt suivant dans la liste
                
                p3 = opt[j]
                p4 = opt[(j+1)%len(opt)]
                
                
                # Si le segment n'est pas vertical
                # On crée la droite passant par le segment
                if (round(p3[0]-p4[0],12) !=0):
                    a2 = (p3[1] - p4[1])/(p3[0]- p4[0]) 
                    b2 = p3[1] - a2*p3[0]
                
                # Si le segment est dans l'axe x
                # On note l'information dans a2
                else : 
                    a2 = None 
                    b2 = p4[0]
                
                if (a1 == a2) : #Les droites sont parallèles, pas d'intersection, fin 
                    continue
                    
                # le robot est dans l'axe x, trouve le pt d'intersection dans ce cas
                if (a1 == None) : 
                    x = b1
                    y = a2*x + b2
                
                # le segment est dans l'axe x, trouve le pt d'intersection dans ce cas
                elif (a2 == None):
                    x = b2
                    y = a1*x + b1
                    
                # Trouve le pt d'intersection des deux droites
                else :
                    x = (b2 - b1) / (a1 - a2)
                    y = a1*x + b1
                
                # Mesure la distance entre le point et l'avant du robot
                res = sqrt(pow(p2[0]-x,2)+pow(p2[1]-y,2))
                
                # On cherche à savoir si le robot est devant
                if mmsigne(p2[0] - p1[0],x - p1[0]) and mmsigne(p2[1] - p1[1],y - p1[1]):
                    
                    # On cherche à savoir si le pt d'intersection est sur le segment
                    if (min(p3[0],p4[0])<=x<=max(p3[0],p4[0]) and 
                        min(p3[1],p4[1])<=y<=max(p3[1],p4[1])):
                        
                        
                        # On regarde si l'objet est à la bonne hauteur pour être detecté
                        h = self.robot.z + (self.robot.hauteur/2)
                        
                        bobj = min(o.z, o.z + o.hauteur)
                        hobj = max(o.z, o.z + o.hauteur)
                        
                        if (h <= hobj and h >= bobj):
                        # Si la distance entre le robot et l'objet est plus petite
                        # que toutes les longueurs mesurées jusqu'à présent
                        # alors c'est que l'objet qu'on examine est devant tous les autres
                            if (mini > res):
                                mini = res

        # On renvoie la distance entre le robot et l'objet le plus proche de lui
        # Si cet objet n'existe pas, renvoie la valeur par défaut 1000000
        return mini 
             
