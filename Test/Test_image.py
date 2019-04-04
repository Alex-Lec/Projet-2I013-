from PIL import Image
import random
import numpy as np


if __name__ == '__main__':
    d = 512
    img = Image.new("RGB", (d, d), "white")
    for i in range(d):
        for j in range(d):
            img.putpixel((i,j), (0,30,50)) 
    
    for i in range(15000):
        img.putpixel((random.randint(0,d-1),random.randint(0,d-1)), \
        (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    
    for i in range(50):
        for j in range(50):
            img.putpixel((i+50,j+50),(255,0,0))
   
          
    img.save("Texture2.jpeg", "jpeg")
    print(img.getpixel((10,10)))
    np.array(img)
    img.show()
