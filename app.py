import numpy as np
import matplotlib.pyplot as plt

total_arrays=[]

def generateMainArray():
    for i in range(1,6):
        array = np.random.randint(low=0, high=255, size=(3, 3))

        generateSecondaryArrays(array)
        total_arrays.append(array)

        for item in generateSecondaryArrays(array):
            total_arrays.append(item)

    generateFigures()

def generateSecondaryArrays(array):
    inner_arrays=[]
    for i in range(2,6):
        secondaryArrays = np.repeat(np.repeat(array, i, axis=0), i, axis=1)
        inner_arrays.append(secondaryArrays)

    return inner_arrays
    
def generateFigures():

    fg = plt.figure(figsize=(10,10))

    for i in range(len(total_arrays)):
        sub = fg.add_subplot(5, 5, i + 1)
        print(total_arrays[i])
        sub.imshow(total_arrays[i], cmap='gray')
        
    plt.show()
 
generateMainArray()