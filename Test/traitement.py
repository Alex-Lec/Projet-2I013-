from PIL import Image
import random
import numpy as np

filtre1 = [[0][1][0]
           [1][1][1]
           [0][1][0]]

filtre2 = [[1][1][1]
           [1][1][1]
           [1][1][1]]

def tret_rec(img,M,x,y):
    cnt = 0
    if (x-1>0):
        (r,g,b) =img.getpixel((x-1,y))
        if (M[x-1][y] == 0 and r >= 250 and g<=0 and b<=0):
            M[x-1][y] = 1
            cnt = cnt + 1 + tret_rec(img,M,x-1,y)

    if (y-1>0):
        (r,g,b) = img.getpixel((x,y-1))
        if (M[x][y-1] == 0 and r >= 250 and g<=0 and b<=0):
            M[x][y-1] = 1
            cnt = cnt + 1 + tret_rec(img,M,x,y-1)

    if (x+1<img.size[0]):
        (r,g,b) = img.getpixel((x+1,y))
        if (M[x+1][y] == 0 and r >= 250 and g<=0 and b<=0):
            M[x+1][y] = 1
            cnt = cnt + 1 + tret_rec(img,M,x+1,y)
  
    if (y+1<img.size[1]):
        (r,g,b) = img.getpixel((x,y+1))
        if (M[x][y+1] == 0 and r >= 250 and g<=0 and b<=0):
            M[x][y+1] = 1
            cnt = cnt + 1 + tret_rec(img,M,x,y+1)
    
    return cnt


def traitement(img):
    (dimx, dimy) = img.size
    max = (-1,-1,-1)
    
    for i in range(dimx):   
        for j in range(dimy):
            (r,g,b) = img.getpixel((i,j))
            if (r >= 250 and g<=0 and b<=0):
                M = np.zeros((dimx,dimy),int)
                M[i][j] = 1
                tmp = tret_rec(img,M,i,j)
                if (tmp > max[0]):
                    max = (tmp, i, j)
                    
                    
    return max

