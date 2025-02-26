import matplotlib.pyplot as plt
import cv2
import numpy as np

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

    A = (r * 0.299)
    B = (g * 0.587)
    C = (b * 0.114)
    gray_image = A + B + C

    gray_image = gray_image.astype(np.uint8)

    m,n = np.shape(gray_image)
    for i in range(0,m):
        for j in range (0,n):
            if gray_image[i,j] < 100:
                gray_image[i,j] = 255
            else:
                gray_image[i,j] = 0

    fg = plt.figure(figsize=(10,10))

    sub = fg.add_subplot(1, 2, 1)
    histogram = cv2.calcHist([np.transpose(gray_image)],[0],None,[255],[0,255]) 
    sub.plot(histogram)
    sub = fg.add_subplot(1, 2, 2)
    sub.imshow(np.invert(gray_image), cmap='gray')
    # sub.imshow(gray_image)
    plt.show()

runSeparation()     