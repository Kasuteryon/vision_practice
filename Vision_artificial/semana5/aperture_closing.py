# CARGAR IMAGEN BGR
# BGR -> RGB
# GRAY
# UMBRALIZAR
# CONTORNOS
# OPERACION MORFOLÓGICAS

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

    # CANNY ----------------------------------------------------------------------

    canny = cv2.Canny(gray_image, 100, 200)
    # kernel para todos
    kernel = np.ones((5,5), np.uint8)
    result_dilate_canny = cv2.dilate(canny, kernel, iterations=1)
    result_erode_canny = cv2.dilate(canny, kernel, iterations=1)


    # IMPRESIÓN
    fg = plt.figure(figsize=(10,10))
    sub = fg.add_subplot(1, 3, 1)
    sub.imshow(gray_image, cmap='gray')
    sub.set_title("Original")

    sub = fg.add_subplot(1, 3, 2)
    sub.imshow(cv2.dilate(result_erode_canny, kernel, iterations=1), cmap='gray')
    sub.set_title("Apertura")

    sub = fg.add_subplot(1, 3, 3)
    sub.imshow(cv2.erode(result_dilate_canny, kernel, iterations=1), cmap='gray')
    sub.set_title("Cierre")

    plt.show()   

run()  