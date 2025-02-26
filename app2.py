import matplotlib.pyplot as plt
import cv2
import numpy as np

def runSeparation():
    image = cv2.imread("./assets/me2.jpg")
    image2 = cv2.imread("./assets/me.jpg")

    image2 = cv2.resize(image2, (3072,4096))

    secondary_image = image.copy()
    secondary_image2 = image2.copy()
   
    b = image[:,:,0] 
    g = image[:,:,1] 
    r = image[:,:,2] 

    b2 = image2[:,:,0] 
    g2 = image2[:,:,1] 
    r2 = image2[:,:,2] 

    # RGB
    secondary_image[:,:,0] = r 
    secondary_image[:,:,1] = g 
    secondary_image[:,:,2] = b 

     # RGB
    secondary_image2[:,:,0] = r2
    secondary_image2[:,:,1] = g2 
    secondary_image2[:,:,2] = b2 
   
    # plt.imshow(secondary_image)

    ## GRAY SCALE

    A = (r * 0.299)
    B = (g * 0.587)
    C = (b * 0.114)
    gray_image = A + B + C

    fg = plt.figure(figsize=(10,10))
    sub = fg.add_subplot(1, 2, 1)

    gray_image = gray_image.astype(np.uint8)

    print(np.max(gray_image))
        
    sub.imshow(gray_image, cmap="gray")
    sub = fg.add_subplot(1, 2, 2)
    histogram = cv2.calcHist([gray_image],[0],None,[256],[0,256]) 
    sub.plot(histogram)
    # sub.imshow(gray_image)

    plt.show()

    # A = ((r * 0.01) + r2)
    # B = ((g * 0.01) + g2)
    # C = ((b * 0.01) + b2)
    # fourth_image = A + B + C
    
    # sub2 = fg.add_subplot(1, 3, 2)
    # sub2.imshow(secondary_image2)

    # sub2 = fg.add_subplot(1, 3, 3)
    # sub2.imshow(fourth_image)


runSeparation()     