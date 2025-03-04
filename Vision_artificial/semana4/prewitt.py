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

    fg = plt.figure(figsize=(10,10))
    
    sub = fg.add_subplot(1, 3, 1)
    sub.imshow(gray_image, cmap='gray')
    sub.set_title("Original Gray")

    sub = fg.add_subplot(1, 3, 2)

    # FILTRO PREWITT
    x = cv2.filter2D(gray_image, cv2.CV_64F, np.array([[-1,0,1],[-1,0,1],[-1,0,1]]))
    y = cv2.filter2D(gray_image, cv2.CV_64F, np.array([[-1,-1,-1],[0,0,0],[1,1,1]]))

    sub.imshow(x, cmap='gray')
    sub.set_title("X-2D")
    
    sub = fg.add_subplot(1, 3, 3)
    sub.imshow(y, cmap='gray')
    sub.set_title("Y-2D")
   
    plt.show()   


run()  