import matplotlib.pyplot as plt
import cv2

def run():
    image = cv2.imread("./assets/me.jpg")
    #imagen, valor inicial, valor maximo
    fg = plt.figure(figsize=(8,8))

    for i in range(1,4):
        sub = fg.add_subplot(1, 3, i)
        histogram = cv2.calcHist([image],[i-1],None,[256],[0,256]) 
        sub.plot(histogram)

    plt.show()

run()