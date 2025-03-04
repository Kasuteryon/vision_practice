import matplotlib.pyplot as plt
import cv2
import numpy as np

def run():
    image = cv2.imread("../../assets/cacao.jpg")

    secondary_image = image.copy()
   
    b = image[:,:,0] 
    g = image[:,:,1] 
    r = image[:,:,2] 
    # RGB
    secondary_image[:,:,0] = r 
    secondary_image[:,:,1] = g 
    secondary_image[:,:,2] = b 
    ## GRAY SCALE

    A = (r * 0.299)
    B = (g * 0.587)
    C = (b * 0.114)
    gray_image = A + B + C

    gray_image = gray_image.astype(np.uint8)
    new_gray = 255 - gray_image

    fg = plt.figure(figsize=(10,10))
    
    sub = fg.add_subplot(1, 3, 1)
    sub.imshow(new_gray, cmap='gray')
    sub.set_title("Original Gray")

    sub = fg.add_subplot(1, 3, 2)

    Sx = cv2.Sobel(new_gray, cv2.CV_64F, 1, 0, ksize=3)
    Sy = cv2.Sobel(new_gray, cv2.CV_64F, 0, 1, ksize=3)

    mag = np.sqrt(Sx**2 + Sy **2)
    sub.imshow(255 - mag, cmap='gray')
    sub.set_title("Magnitud")
    
    sub = fg.add_subplot(1, 3, 3)
    sub.imshow(255 - (1/mag), cmap='gray')
    sub.set_title("Magnitud Inversa")
   
    plt.show()   


run()  