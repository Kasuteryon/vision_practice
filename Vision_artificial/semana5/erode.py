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
    result_canny = cv2.erode(canny, kernel, iterations=1)

    # SOBEL ----------------------------------------------------------------------

    # UMBRALIZAR (PARA AMBOS)
    m,n = np.shape(gray_image)
    for i in range(0,m):
        for j in range (0,n):
            if gray_image[i,j] < 127:
                gray_image[i,j] = 255
            else:
                gray_image[i,j] = 0


    Sx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    Sy = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
    sobel = np.sqrt(Sx**2 + Sy **2)

    result_sobel = cv2.erode(sobel, kernel, iterations=1)
    # ----------------------------------------------------------------------------

    # PREWITT --------------------------------------------------------------------

    # FILTRO PREWITT (CONTORNO)
    x = cv2.filter2D(gray_image, cv2.CV_64F, np.array([[-1,0,1],[-1,0,1],[-1,0,1]]))
    y = cv2.filter2D(gray_image, cv2.CV_64F, np.array([[-1,-1,-1],[0,0,0],[1,1,1]]))

    #  OPERACIÓN MORFOLÓFICA
    filtered_prewitt_image = x + y
    result_prewitt = cv2.erode(filtered_prewitt_image, kernel, iterations=1)

    # ----------------------------------------------------------------------------

    # IMPRESIÓN
    fg = plt.figure(figsize=(10,10))
    sub = fg.add_subplot(1, 4, 1)
    sub.imshow(filtered_prewitt_image, cmap='gray')
    sub.set_title("Antes Erosión")

    sub = fg.add_subplot(1, 4, 2)
    sub.imshow(result_prewitt, cmap='gray')
    sub.set_title("Después de Erosión Prewitt")

    sub = fg.add_subplot(1, 4, 3)
    sub.imshow(result_sobel, cmap='gray')
    sub.set_title("Después de Erosión Sobel")

    sub = fg.add_subplot(1, 4, 4)
    sub.imshow(result_canny, cmap='gray')
    sub.set_title("Después de Erosión canny")

    plt.show()   

run()  