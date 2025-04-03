import numpy as np
import matplotlib.pyplot as plt

def run():
    x = np.array([1,2,3,4,5])

    y = np.array([0.8,1.3,3.2,4.5,6.2])

    n = len(x)

    a1, a0 = calculateA(x,y,n)
   
    print(a1)

    print(a0)

    # plt.figure(figsize=(10,10))
    # plt.scatter(x, y, color="blue", label="Origin Data")

    # # sub.set_title("Original")
    # plt.show()

def calculateA(x, y, n):
    sumy= 0
    sumx= 0
    sumxy = 0
    sumxpow = 0
 
    for i in range(len(x)):
        sumx = sumx + x[i]
        sumy = sumy + y[i]
        sumxy = sumxy + (x[i] * y[i])
        sumxpow = sumxpow + (x[i]**2)

    print("---SUMX")
    print(sumx)
    print("---SUMy")
    print(sumy)
    print("---SUMXY")
    print(sumxy)
    print("---SUMX POW")
    print(sumxpow)
    sum2x  =sumx**2
    print("--- SUM 2X")
    print(sum2x)

    a1 = ((n*sumxy)-(sumx*sumy))  / ((n*sumxpow)-(sum2x))

    a0 = (sumy/n) - (a1 * (sumx/n)) 

    return a1, a0

run()