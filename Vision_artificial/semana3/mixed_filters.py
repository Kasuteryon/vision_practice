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
    
    sub = fg.add_subplot(1, 4, 1)
    sub.imshow(secondary_image)
    sub.set_title("Original")

    sub = fg.add_subplot(1, 4, 2)
    mixed = noise.add_salt_and_pepper_noise(noise.add_gaussian_noise(secondary_image))
    sub.imshow(mixed)
    sub.set_title("Ruido Mixto")
    
    # COLUMN 2
   
    sub = fg.add_subplot(1, 4, 3)
    sub.imshow(cv2.GaussianBlur(cv2.medianBlur(mixed, 5),(3,3),0))
    sub.set_title("MedianBlur > Gaussian")

    sub = fg.add_subplot(1, 4, 4)
    sub.imshow(cv2.medianBlur(cv2.GaussianBlur(mixed,(3,3),0), 5))
    sub.set_title("Gaussian > MedianBlur")

    plt.show()   


run()  