from math import sqrt
from principal import Terrain as t

class Detecteur:
    
    def __init__(self, robot):
        pass
        
    def detecter(self,rob, obj): #prend une liste d'objetphysique en arguement et un robot'

        def mmsigne(a,b):
            if (a<0 and b<0):
                return True
            if (a==0 and b==0):
                return True
            return (a>0 and b>0)
            
        mini = 1000000
        p1 = (rob.x,rob.y)
        p2 = (rob.x + (rob.largeur /2)*rob.vecteur_direction.x,
              rob.y + (rob.largeur /2)*rob.vecteur_direction.y)
        
        if (p1[0]-p2[0] != 0): 
            a1 = (p1[1] - p2[1]) /(p1[0]- p2[0])
            b1 = p1[1] - a1*p1[0]
        else :
            a1 = None # Cas ou le robot est dans l'axe x
            b1 = p1[0]
            
        for o in obj:
            for j in range(len(o.points)):
                p3 = o.points[j]
                p4 = o.points[(j+1)%len(o.points)]#Marche avec un polygone à n cotées
                
                if (p3[0]-p4[0] !=0):
                    a2 = (p3[1] - p4[1])/(p3[0]- p4[0]) 
                    b2 = p3[1] - a2*p3[0]
                
                else :
                    a2 = None # Cas ou le segment est dans l'axe x
                    b2 = p4[0]
                
                if (a1 == a2) :
                    continue
                
                if (a1 == None) :
                    x = b1
                    y = a2*x + b2
                
                elif (a2 == None):
                    x = b2
                    y = a1*x + b1
                
                else :
                    x = (b2 - b1) / (a1 - a2)
                    y = a1*x + b1
                
                res = sqrt(pow(p2[0]-x,2)+pow(p2[1]-y,2))
                
                if mmsigne(p2[0] - p1[0],x - p1[0]) and mmsigne(p2[1] - p1[1],y - p1[1]):
                    
                    if (min(p3[0],p4[0])<=x<=max(p3[0],p4[0]) and 
                        min(p3[1],p4[1])<=y<=max(p3[1],p4[1])):
                        if (mini > res):
                            mini = res
            
        return mini
             