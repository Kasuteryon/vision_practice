import cv2
from datetime import datetime
import matplotlib.pyplot as plt

def init():
    camera = cv2.VideoCapture(1)

    ret, frame = camera.read(1)

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
    border= cv2.Canny(gray, 100, 200)

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
    sub.set_title("Aplicación de Canny")

    sub = fg.add_subplot(1, 3, 3)
    sub.imshow(contours2)
    sub.set_title("Encontrando Contornos")

    plt.show()

init()