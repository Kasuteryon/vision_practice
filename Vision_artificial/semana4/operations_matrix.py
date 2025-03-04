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

    fg = plt.figure(figsize=(10,10))
    
    sub = fg.add_subplot(1, 4, 1)
    sub.imshow(secondary_image)
    sub.set_title("Original")

    sub = fg.add_subplot(1, 4, 2)
    sum = secondary_image + 10
    sub.imshow(sum)
    sub.set_title("Suma")
    
    sub = fg.add_subplot(1, 4, 3)
    minus = secondary_image - 10
    sub.imshow(minus)
    sub.set_title("Resta")

    sub = fg.add_subplot(1, 4, 4)
    multiply = secondary_image * 10
    sub.imshow(multiply)
    sub.set_title("Multiplicación")

    plt.show()   


run()  