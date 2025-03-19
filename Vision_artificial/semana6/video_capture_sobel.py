import cv2
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

def init():
    camera = cv2.VideoCapture(0)

    ret, frame = camera.read(0)

    if ret:
        name = 'img'+"_"+str(datetime.now())+".jpg";
        cv2.imwrite(name, frame)
        extractBorders(name=name)
        print("Saved Image")
    else:
        print("Error in Camera")
       
    camera.release()
    cv2.destroyAllWindows()

def extractBorders(name):
    image = cv2.imread(name)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    border= sobel(gray_image=gray)

    # Solo vamos a necesitar el primer valor, el "_" lo usamos para poder tener el requisito
    # como tupla a pesar que no se usará ese segundo valor
    contours, _ = cv2.findContours(border, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Param: Imagen, contorno, profundida, color, grosor
    contours2 = cv2.drawContours(image, contours, -1, (0,255,0), 2)

    graph(image_rgb=image_rgb, border=border, contours2=contours2)

def graph(image_rgb, border, contours2):
    fg = plt.figure(figsize=(10,10))

    sub = fg.add_subplot(1, 3, 1)
    sub.imshow(image_rgb)
    sub.set_title("Original")

    sub = fg.add_subplot(1, 3, 2)
    sub.imshow(border, cmap="gray")
    sub.set_title("Aplicación de Sobel")

    sub = fg.add_subplot(1, 3, 3)
    sub.imshow(contours2)
    sub.set_title("Encontrando Contornos")

    plt.show()

def sobel(gray_image):
    Sx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    
    Sy = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)

    mag = np.sqrt(Sx**2 + Sy **2)

    return mag

init()