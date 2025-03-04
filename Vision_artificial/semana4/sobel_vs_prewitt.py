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

    # Calculos

    # FILTRO PREWITT
    x = cv2.filter2D(gray_image, cv2.CV_64F, np.array([[-1,0,1],[-1,0,1],[-1,0,1]]))
    y = cv2.filter2D(gray_image, cv2.CV_64F, np.array([[-1,-1,-1],[0,0,0],[1,1,1]]))
    prewitt_mag = np.sqrt(x**2 + y **2)

    # FILTRO SOBEL
    Sx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=7)
    Sy = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=7)
    sobel_mag = np.sqrt(Sx**2 + Sy **2)
    # Plot

    fg = plt.figure(figsize=(12, 10))

    # PREWITT
    
    sub = fg.add_subplot(1, 3, 1)
    sub.imshow(x, cmap='gray')
    sub.set_title("X Prewitt")

    sub = fg.add_subplot(1, 3, 2)
    sub.imshow(y, cmap='gray')
    sub.set_title("Y Prewitt")
    
    sub = fg.add_subplot(1, 3, 3)
    sub.imshow(prewitt_mag, cmap='gray')
    sub.set_title("Magnitud Prewitt")

    # SOBEL

    sub = fg.add_subplot(2, 3, 1)
    sub.imshow(Sx, cmap='gray')
    sub.set_title("X Sobel")

    sub = fg.add_subplot(2, 3, 2)
    sub.imshow(Sy, cmap='gray')
    sub.set_title("Y Sobel")
    
    sub = fg.add_subplot(2, 3, 3)
    sub.imshow(sobel_mag, cmap='gray')
    sub.set_title("Magnitud Sobel")
   
    plt.show()   


run()  