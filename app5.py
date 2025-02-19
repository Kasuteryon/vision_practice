import matplotlib.pyplot as plt
import cv2

def run():

    image = cv2.imread("./assets/me.jpg")

    #imagen, valor inicial, valor maximo

    fg = plt.figure(figsize=(8,8))

    sub = fg.add_subplot(1, 3, 1)
    histogram1 = cv2.calcHist([image],[0],None,[256],[0,256]) 
    sub.plot(histogram1)

    sub = fg.add_subplot(1, 3, 2)
    histogram2 = cv2.calcHist([image],[1],None,[256],[0,256]) 
    sub.plot(histogram2)

    sub = fg.add_subplot(1, 3, 3)
    histogram3 = cv2.calcHist([image],[2],None,[256],[0,256]) 
    sub.plot(histogram3)

    plt.show()

run()