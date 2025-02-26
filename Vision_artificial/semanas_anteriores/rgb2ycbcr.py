import matplotlib.pyplot as plt
import cv2
import numpy as np

def runSeparation():
    image = cv2.imread("./assets/me2.jpg")

    cbcr = image.copy()
   
    b = image[:,:,0] 
    g = image[:,:,1] 
    r = image[:,:,2] 

    # RGB
    cbcr[:,:,0] = r 
    cbcr[:,:,1] = g 
    cbcr[:,:,2] = b 

    # Imagen original de BGR -> RGB
    fg = plt.figure(figsize=(10,10))
    sub = fg.add_subplot(1, 2, 1)
    sub.imshow(cbcr)
    
    # RGB -> YCbCr
    cbcr[:,:,0] = .299 * r + .587 * g + .114 * b
    # Cb
    cbcr[:,:,1] = 128 - .169 * r - .331 * g + .5 * b
    # Cr
    cbcr[:,:,2] = 128 + .5 * r - .419 * g - .081 * b

    # Mostrar Imagen 2
    sub = fg.add_subplot(1, 2, 2)
    sub.imshow(cbcr)

    plt.show()

runSeparation()     