from PIL import Image
import random
import numpy as np


if __name__ == '__main__':
    d = 512
    img = Image.new("RGB", (d, d), "white")
    for i in range(d):
        for j in range(d):
            img.putpixel((i,j), (0,0,0)) 
    
    
    for i in range(15000):
        img.putpixel((random.randint(0,d-1),random.randint(0,d-1)), \
        (random.randint(0,255), random.randint(0,20), random.randint(0,20)))
    """
    for i in range(120):
        for j in range(100):
            img.putpixel((i+300,j+200),(255,0,0))
    """
          
    img.save("Texture2.jpeg", "jpeg")
    print(img.getpixel((10,10)))
    np.array(img)
    img.show()
