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


    fg = plt.figure(figsize=(10,10))
    
    sub = fg.add_subplot(1, 4, 1)
    sub.imshow(gray_image, cmap='gray')
    sub.set_title("Original Gray")

    sub = fg.add_subplot(1, 4, 2)
    Sx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    sub.imshow(Sx, cmap='gray')
    sub.set_title("Sx")
    
    sub = fg.add_subplot(1, 4, 3)
    Sy = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
    sub.imshow(Sy, cmap='gray')
    sub.set_title("Sy")

    sub = fg.add_subplot(1, 4, 4)
    mag = np.sqrt(Sx**2 + Sy **2)
    sub.imshow(1/mag, cmap='gray')
    sub.set_title("Magnitud")

    plt.show()   


run()  