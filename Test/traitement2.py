from PIL import Image
import random
import numpy as np

"""filtre1 = [[0][1][0]
           [1][1][1]
           [0][1][0]]

filtre2 = [[1][1][1]
           [1][1][1]
           [1][1][1]]"""

def vbas(img,x,y,cpt):
    (r,g,b) = img.getpixel((x,y+1))
    if (y+1<img.size[1] and r >= 250 and g<=0 and b<=0 ):
            #M[x][y+1] = 1
            vbas(img,x,y+1,cpt+1)
    else:
        return cpt


def tret_rec(img,x,y,cpt,cpt_x,x2):
    (r,g,b) = img.getpixel((x+1,y))
    if (x+1<img.size[0]  and r >= 250 and g<=0 and b<=0 ):
        tret_rec(img,x+1,y,cpt+1+vbas(img,x+1,y,0),cpt_x+1,x2)
    else:
        return (cpt,cpt_x,x2)

def tret(img,x,y):
    return tret_rec(img,x,y,0,0,x)


def traitement(img):
    (dimx, dimy) = img.size
    max=(-1,-1,-1)
    for i in range(dimx):
        for j in range(dimy):
            (r,g,b) = img.getpixel((i,j))
            if (r >= 250 and g<=0 and b<=0):
                tmp = tret(img,i,j,i)
                if (tmp[0] > max[0]):
                    max = (tmp, i, j)
    return max[2]+max[1]/2
