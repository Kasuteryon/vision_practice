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

    img_hsv = cv2.cvtColor(secondary_image, cv2.COLOR_RGB2HSV)

    fg = plt.figure(figsize=(10,10))
    
    sub = fg.add_subplot(1, 4, 1)
    sub.imshow(img_hsv)
    sub.set_title("HSV")

    sub = fg.add_subplot(1, 4, 2)
    sum = img_hsv + 10
    sub.imshow(sum)
    sub.set_title("HSV Suma")
    
    sub = fg.add_subplot(1, 4, 3)
    minus = img_hsv - 10
    sub.imshow(minus)
    sub.set_title("HSV Resta")

    sub = fg.add_subplot(1, 4, 4)
    multiply = img_hsv * 10
    sub.imshow(multiply)
    sub.set_title("HSV Multiplicación")

    plt.show()   


run()  