import matplotlib.pyplot as plt
import cv2
import numpy as np
import gaussian_noise as noise

def run():
    image = cv2.imread("./assets/me2.jpg")

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
    sub = fg.add_subplot(1, 3, 3)
    sub.imshow(noise.add_salt_and_pepper_noise(secondary_image))
    sub.set_title("Ruido Sal y Pimienta")

    plt.show()   


run()  