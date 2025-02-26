import matplotlib.pyplot as plt
import cv2
import numpy as np
import math

def runSeparation():
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

    sub = fg.add_subplot(1, 2, 1)
    sub.imshow(secondary_image, cmap='gray')
  
    sub = fg.add_subplot(1, 2, 2)
    sub.imshow(imageRotation(secondary_image, 45), cmap='gray')
    # sub.imshow(gray_image)
    plt.show()   

def imageRotation(image, degree):
    # First we will convert the degrees into radians
    rads = math.radians(degree)

    # We consider the rotated image to be of the same size as the original
    rot_img = np.uint8(np.zeros(image.shape))

    # Finding the center point of rotated (or original) image.
    height = rot_img.shape[0]
    width  = rot_img.shape[1]

    midx,midy = (width//2, height//2)

    for i in range(rot_img.shape[0]):
        for j in range(rot_img.shape[1]):
            x= (i-midx)*math.cos(rads)+(j-midy)*math.sin(rads)
            y= -(i-midx)*math.sin(rads)+(j-midy)*math.cos(rads)

            x=round(x)+midx 
            y=round(y)+midy 

            if (x>=0 and y>=0 and x<image.shape[0] and  y<image.shape[1]):
                rot_img[i,j,:] = image[x,y,:]

    return rot_img 


runSeparation()  