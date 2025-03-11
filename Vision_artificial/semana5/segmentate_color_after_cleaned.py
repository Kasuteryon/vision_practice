# Quitar ruido

# Segmentar por bordes

# Segmentar por color
    # Wall E (naranja - amarillo)
    # Rayo McQueen (Rojo)

import matplotlib.pyplot as plt
import cv2
import numpy as np

def run():
    rasho = cv2.imread("../../assets/rayo_ruido.jpg")
    walle = cv2.imread("../../assets/walle_ruido.jpg")

    secondary_rasho = rasho.copy()
    secondary_walle = walle.copy()

    third_rasho = cv2.medianBlur(secondary_rasho,5)
    third_walle = cv2.medianBlur(secondary_walle,5)

    fourth_rasho = third_rasho.copy()
    fourth_walle = third_walle.copy()
   
    b = third_rasho[:,:,0] 
    g = third_rasho[:,:,1] 
    r = third_rasho[:,:,2] 

    b2 = third_walle[:,:,0] 
    g2 = third_walle[:,:,1] 
    r2 = third_walle[:,:,2] 
    # RGB
    fourth_rasho[:,:,0] = r 
    fourth_rasho[:,:,1] = g 
    fourth_rasho[:,:,2] = b 

    fourth_walle[:,:,0] = r2
    fourth_walle[:,:,1] = g2 
    fourth_walle[:,:,2] = b2 
    

    rasho_hsv = cv2.cvtColor(fourth_rasho, cv2.COLOR_RGB2HSV)
    walle_hsv = cv2.cvtColor(fourth_walle, cv2.COLOR_RGB2HSV)

    # GRAY

    A = (r * 0.299)
    B = (g * 0.587)
    C = (b * 0.114)
    gray_rasho = A + B + C

    gray_rasho = gray_rasho.astype(np.uint8)

    A2 = (r2 * 0.299)
    B2 = (g2 * 0.587)
    C2 = (b2 * 0.114)
    gray_walle = A2 + B2 + C2

    gray_rasho = gray_rasho.astype(np.uint8)
    gray_walle = gray_walle.astype(np.uint8)

    ## COLOR RASHO 1 (ROJO)

    low_rasho = np.array([0, 100, 100])
    high_rasho = np.array([1, 255, 255])

    mask_rasho = cv2.inRange(rasho_hsv, low_rasho, high_rasho)

    seg_rasho = cv2.bitwise_and(fourth_rasho, fourth_rasho, mask=mask_rasho)

    ## COLOR RASHO 2 (ROJO)

    low_rasho_2 = np.array([170, 100, 100])
    high_rasho_2 = np.array([180, 255, 255])

    mask_rasho_2 = cv2.inRange(rasho_hsv, low_rasho_2, high_rasho_2)

    seg_rasho_2 = cv2.bitwise_and(fourth_rasho, fourth_rasho, mask=mask_rasho_2)

    ## COLOR RASHO 3 (NARANJA)

    low_rasho_3 = np.array([10, 100, 100])
    high_rasho_3 = np.array([25, 255, 255])

    mask_rasho_3 = cv2.inRange(rasho_hsv, low_rasho_3, high_rasho_3)

    seg_rasho_3 = cv2.bitwise_and(fourth_rasho, fourth_rasho, mask=mask_rasho_3)

    # COLOR PARA WALLE 1 (NARANJA)

    low_walle = np.array([10, 100, 100])
    high_walle = np.array([25, 255, 255])

    mask_walle = cv2.inRange(walle_hsv, low_walle, high_walle)

    seg_walle = cv2.bitwise_and(fourth_walle, fourth_walle, mask=mask_walle)

    # COLOR PARA WALLE 2 (ROJO)

    low_walle_2 = np.array([170, 100, 100])
    high_walle_2 = np.array([180, 255, 255])

    mask_walle_2 = cv2.inRange(walle_hsv, low_walle_2, high_walle_2)

    seg_walle_2 = cv2.bitwise_and(fourth_walle, fourth_walle, mask=mask_walle_2)

    # COLOR PARA WALLE 3 (AMARILLO)

    low_walle_3 = np.array([25, 100, 100])
    high_walle_3= np.array([35, 255, 255])

    mask_walle_3 = cv2.inRange(walle_hsv, low_walle_3, high_walle_3)

    seg_walle_3 = cv2.bitwise_and(fourth_walle, fourth_walle, mask=mask_walle_3)

    # COLOR PARA WALLE 4 (VERDE)

    low_walle_4 = np.array([35, 100, 100])
    high_walle_4 = np.array([85, 255, 255])

    mask_walle_4 = cv2.inRange(walle_hsv, low_walle_4, high_walle_4)

    seg_walle_4 = cv2.bitwise_and(fourth_walle, fourth_walle, mask=mask_walle_4)

    # FILTRO PARA BORDES
    Sx = cv2.Sobel(gray_rasho, cv2.CV_64F, 1, 0, ksize=7)
    Sy = cv2.Sobel(gray_rasho, cv2.CV_64F, 0, 1, ksize=7)
    sobel_mag_rasho = np.sqrt(Sx**2 + Sy **2)

    Sx = cv2.Sobel(gray_walle, cv2.CV_64F, 1, 0, ksize=7)
    Sy = cv2.Sobel(gray_walle, cv2.CV_64F, 0, 1, ksize=7)
    sobel_mag_walle = np.sqrt(Sx**2 + Sy **2)


    # SHOW EVERYTHING
    fg = plt.figure(figsize=(10,10))

    sub = fg.add_subplot(2, 3, 1)
    sub.imshow(fourth_rasho)
    sub.set_title("Limpieza Rayo")

    sub = fg.add_subplot(2, 3, 2)
    sub.imshow(sobel_mag_rasho)
    sub.set_title("Bordes Rayo")

    sub = fg.add_subplot(2, 3, 3)
    sub.imshow(seg_rasho +seg_rasho_2 +seg_rasho_3)
    sub.set_title("Color Rayo")

    sub = fg.add_subplot(2, 3, 4)
    sub.imshow(cv2.medianBlur(fourth_walle,5))
    sub.set_title("Limpieza WallE")
    
    sub = fg.add_subplot(2, 3, 5)
    sub.imshow(sobel_mag_walle)
    sub.set_title("Bordes WallE")

    sub = fg.add_subplot(2, 3, 6)
    sub.imshow(seg_walle + seg_walle_2 + seg_walle_3 + seg_walle_4)
    sub.set_title("Color WallE")

    plt.show()   

run()  