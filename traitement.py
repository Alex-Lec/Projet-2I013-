import cv2
import numpy as np
import time

img = cv2.imread('screen_8.jpeg')
(dimy, dimx,unused) = img.shape

def trait_red(img,x,y):
    cpt = 0
    if (x+2<dimx):
        (b,g,r) = img[y,x+2]
    while (x+2<dimx  and (r >= 150 and g<=100 and b<=100) ):
        (b,g,r) = img[y,x+2]
        x+=2
        cpt+=1
    return cpt

def trait_green(img,x,y):
    cpt = 0
    if (x+2<dimx):
        (b,g,r) = img[y,x+2]
    while (x+2<dimx  and (g>=110 and g > r +40 and g > b +40) ):
        (b,g,r) = img[y,x+2]
        x+=2
        cpt+=2
    return cpt

"""def traitement_red(img):
    max_r=(-1,-1)
    for i in range(dimx):
        for j in range(dimy):
            (b,g,r) = img[j,i]
            if (r >= 150 and g<=100 and b<=100):
                tmp_r = (trait_red(img,i,j),i)
                i+= tmp_r[0]
                if (tmp_r[0] > max_r[0]):
                    max_r = tmp_r
    return max_r[1]+max_r[0]//2

def traitement_green(img):
    max =(-1,-1)
    for i in range(0,dimx,2):
        for j in range(0,dimy,2):
            (b,g,r) = img[j,i]
            if (g>=110 and g > r +40 and g > b +40):
                tmp = (trait_green(img,i,j),i)
                i+= tmp[0]
                if (tmp[0] > max[0]):
                    max = tmp
    return max[1]+max[0]//2"""



def traitement(img):
    max_r=(-1,-1)
    max_g=(-1,-1)

    for i in range(0,dimx,2):
        for j in range(0,dimy,2):
            (b,g,r) = img[j,i]
            if (r >= 150 and g<=100 and b<=100):
                tmp_r = (trait_red(img,i,j),i)
                i += tmp_r[0]
                if (tmp_r[0] > max_r[0]):
                    max_r = tmp_r
            if (g>=110 and g > r +40 and g > b +40):
                tmp_g = (trait_green(img,i,j),i)
                i+= tmp_g [0]
                if (tmp_g[0] > max_g[0]):
                    max_g = tmp_g

    return ((max_r[1]+max_r[0]//2) +(max_g[1]+max_g[0]//2)) //2

def ligne(img,x):
    for i in range (3):
        for j in range (dimy):
            img[j,x-1+i] =[0,0,0]


ligne(img,traitement(img))
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
