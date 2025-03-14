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

    secondary_rasho = rasho.copy()

    third_rasho = cv2.medianBlur(secondary_rasho,5)

    fourth_rasho = third_rasho.copy()
   
    b = third_rasho[:,:,0] 
    g = third_rasho[:,:,1] 
    r = third_rasho[:,:,2] 

    # RGB
    fourth_rasho[:,:,0] = r 
    fourth_rasho[:,:,1] = g 
    fourth_rasho[:,:,2] = b 

    rasho_hsv = cv2.cvtColor(fourth_rasho, cv2.COLOR_RGB2HSV)

    # GRAY

    A = (r * 0.299)
    B = (g * 0.587)
    C = (b * 0.114)
    gray_rasho = A + B + C

    gray_rasho = gray_rasho.astype(np.uint8)

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

    # DILATAR

    kernel = np.ones((5,5), np.uint8)
    result_dilate = cv2.dilate(mask_rasho, kernel, iterations=4)

    
    
    seg_rasho4 = cv2.bitwise_and(fourth_rasho, fourth_rasho, mask=result_dilate)
    
    # SHOW EVERYTHING


    fg = plt.figure(figsize=(10,10))

    sub = fg.add_subplot(1, 2, 1)
    sub.imshow(fourth_rasho)
    sub.set_title("Rayo sin Dilatar")

    sub = fg.add_subplot(1, 2, 2)
    sub.imshow(seg_rasho4)
    sub.set_title("Bordes Rayo")


    plt.show()   

run()  