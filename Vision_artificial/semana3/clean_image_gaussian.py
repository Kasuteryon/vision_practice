import matplotlib.pyplot as plt
import cv2
import numpy as np
import gaussian_noise as noise

def run():
    image = cv2.imread("../../assets/me2.jpg")

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

    sub = fg.add_subplot(1, 3, 1)
    sub.imshow(secondary_image)
    sub.set_title("Original")

    sub = fg.add_subplot(1, 3, 2)
    sub.imshow(noise.add_gaussian_noise(secondary_image))
    sub.set_title("Ruido Gaussiano")
    
    # ---- ROW 2

    plt.tight_layout()

    sub = fg.add_subplot(2, 3, 1)
    sub.imshow(secondary_image)
    sub.set_title("Original")

    sub = fg.add_subplot(2, 3, 2)
    # In cv2.GaussianBlur(image,(3,3),0) Parameter 1 is image, parameter 2 is kernel, parameter 3 is sigma
    sub.imshow(cv2.GaussianBlur(noise.add_gaussian_noise(secondary_image),(9,9),1))
    sub.set_title("Ruido Gaussiano (Limpio)")

    plt.show()   


run()  