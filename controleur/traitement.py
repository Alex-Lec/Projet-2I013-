from PIL import Image
import random
import numpy as np


def tret3D(img,a,b):
    L = [(a,b)]
    M = np.zeros((img.size[0],img.size[1]),int)
    M[a][b] = 1
    
    for (x,y) in L:
        if (x-1>0):
            (r,g,b) = img.getpixel((x-1,y))
            if (M[x-1][y] == 0):
                if (r >= 200 and g<=0 and b<=0):
                    L += [(x-1,y)]
                    M[x-1][y] = 1
                else : break
        else : break
                
        if (y-1>0):
            (r,g,b) = img.getpixel((x,y-1))
            if (M[x][y-1] == 0):
                if (r >= 200 and g<=0 and b<=0):
                    L += [(x,y-1)]
                    M[x][y-1] = 1
                else : break
        else : break
        
        if (x+1<img.size[0]):
            (r,g,b) = img.getpixel((x+1,y))
            if (M[x+1][y] == 0):
                if (r >= 200 and g<=0 and b<=0):
                    L += [(x+1,y)]
                    M[x+1][y] = 1
                else : break
        else : break
        
        
        if (y+1<img.size[1]):
            (r,g,b) = img.getpixel((x,y+1))
            if (M[x][y+1] == 0):
                if (r >= 200 and g<=0 and b<=0):
                    L += [(x,y+1)]
                    M[x][y+1] = 1
                else : break
        else : break  
    
    p = np.poly1d([2,2,1-len(L)])
    return np.floor(p.roots[1])

def traitement_Champi(img):
    (dimx, dimy) = img.size
    max = (-1,-1,-1)
    
    t = time.time()
    for i in range(dimx):   
        for j in range(dimy):
        
            (r,g,b) = img.getpixel((i,j))
            if (r >= 230 and g<=0 and b<=0):
                tmp = tret3D(img,i,j)
                if (tmp > max[0]):
                    max = (tmp, i, j)
    
    print(time.time() - t)
                    
    return max

def traitement_Moy(img):
    (dimx, dimy) = img.size
    res = 0
    open = False
    cnt = 0
    deb = 0
    nbp = 0
    #t = time.time()
    for i in range(dimy):   
        for j in range(dimx):
            (r,g,b) = img.getpixel((j,i))
            
            if (r >= 230 and g<20 and b<20):
                if not open:
                    open = True
                    cnt = 1
                    deb = j  
                else:
                    cnt += 1
            elif open :
                res /= cnt
                res += (j+deb)/2
                open = False
                nbp += cnt
    
    #print (time.time() - t)      
    return (res,nbp)
    
    
    
    
    
    
    
    
    
    
