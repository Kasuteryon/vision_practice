import matplotlib.pyplot as plt
import cv2
import numpy as np

def run():
    image = cv2.imread("../../assets/me.jpg")

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

    low = np.array([0, 50, 50])
    high = np.array([10, 255, 255])

    mask = cv2.inRange(img_hsv, low, high)

    seg = cv2.bitwise_and(secondary_image, secondary_image, mask=mask)

    fg = plt.figure(figsize=(10,10))
    sub = fg.add_subplot(1, 2, 1)
    sub.imshow(mask, cmap='gray')
    sub.set_title("Máscara")

    sub = fg.add_subplot(1, 2, 2)
    sub.imshow(seg)
    sub.set_title("Ejemplo Bitwise")

    plt.show()   


run()  