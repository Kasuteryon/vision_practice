import matplotlib.pyplot as plt
import cv2

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

    # GRAY SCALE

    # A = (r * 0.299)
    # B = (g * 0.587)
    # C = (b * 0.114)
    # third_image = A + B + C

    A = ((r * 0.01) + r2)
    B = ((g * 0.01) + g2)
    C = ((b * 0.01) + b2)
    fourth_image = A + B + C

    fg = plt.figure(figsize=(10,10))

    sub = fg.add_subplot(1, 3, 1)
    sub.imshow(1/A, cmap="Reds")
    
    sub2 = fg.add_subplot(1, 3, 2)
    sub2.imshow(1/B, cmap="Greens")

    sub3 = fg.add_subplot(1, 3, 3)
    sub3.imshow(1/C, cmap="Blues")

    plt.show()

runSeparation()     