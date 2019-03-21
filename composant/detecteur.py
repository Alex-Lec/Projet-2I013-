from math import sqrt

class Detecteur:
    
    def __init__(self, robot):
        self.robot = robot
        
    def detecte(self):
        """
        Mesure la distance entre le devant du robot et les objets devant.
        Retourne seulement l'objet dans la bonne direction et le plus proche du robot
        DETECTE LES AUTRES ROBOTS
        
        NE MARCHE QUE SI ROBOT A UNE robot.arene !!!
        """
    
        if (self.robot.arene == None):
            return
        
        obj = self.robot.arene.objet + self.robot.arene.robot
        
        def mmsigne(a,b): 
            if (a<0 and b<0):
                return True
            if (a==0 and b==0):
                return True
            return (a>0 and b>0)
            
        mini = 1000000
        p1 = (self.robot.x,self.robot.y)
        p2 = (self.robot.x + (self.robot.longueur /2)*self.robot.v_dir.x,
              self.robot.y + (self.robot.longueur /2)*self.robot.v_dir.y)
        
        if (round(p1[0]-p2[0],12) != 0): 
            a1 = (p1[1] - p2[1]) /(p1[0]- p2[0])
            b1 = p1[1] - a1*p1[0]
        else :
            a1 = None # Cas ou le robot est dans l'axe x
            b1 = p1[0]
            
        for o in obj:
            if (o == self.robot):
                continue
                
            o = o.get_points()
            for j in range(len(o)):
                p3 = o[j]
                p4 = o[(j+1)%len(o)]#Marche avec un polygone à n cotées
                
                if (round(p3[0]-p4[0],12) !=0):
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
             
