from math import sqrt

class Detecteur:
    
    def __init__(self):
        pass
        
    def detecter(rob, obj): #prend une liste d'objetphysique en arguement et un robot'

        def mmsigne(a,b):
            if (a<=0 and b<=0):
                return True
            return (a>=0 and b>=0)
            
        mini = 100000000000
        p1 = (rob.x,rob.y)
        p2 = (rob.vecteur_direction.x,rob.vecteur_direction.y)
        
        if (p1[0]-p2[0] != 0): 
            a1 = (p1[1] - p2[1]) /(p1[0]- p2[0])
            b1 = p1[1] - a1*p1[0]
        else :
            a1 = None
            b1 = p1[0]
            
        for o in obj:
        
            for j in range(len(o.points)):
                p3 = o.points[j]
                p4 = o.points[(j+1)%len(o.points)]
                
                if (p3[0]-p4[0] !=0):
                    a2 = (p3[1] - p4[1])/(p3[0]- p4[0]) 
                    b2 = p3[1] - a2*p3[0]
                
                else :
                    a2 = None
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
                
                res = sqrt(pow(p1[0]-x,2)+pow(p1[1]-y,2))
                
                if mmsigne(p2[0] - p1[0],x) and mmsigne(p2[1] - p1[1],y):
                    if (mini < res):  
                        mini = res
            
        return 
             
