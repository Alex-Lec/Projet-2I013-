from math import sqrt

class Detecteur:
    
    def __init__(self):
        pass
        
    def detecter(rob, obj):
        mini = 100000000000
        
        p1 = (rob.x,rob.y)
        p2 = (rob.vecteur_direction.x,rob.vecteur_direction.y)
        
        a1 = (p1.x- p2.x) / (p1.y - p2.y)
        b1 = p1.y - a1*p1.x
        
        for j in range(len(o.points)):
            p3 = o.points[j]
            p4 = o.points[(j+1)%len(o.points)]
            
            a2 = (p3.x- p4.x) / (p3.y - p4.y)
            b2 = p3.y - a2*p3.x
            
            if (a1 == a2) :
                continue
            
            x = (b2 - b1) / (a1 - a2)
            
            y = a1*x + b1
            
            res = sqrt(pow(p1.x-x,2)+pow(p1.y-y,2))
            
            if (mini < res):
                mini = res
            
       
             
