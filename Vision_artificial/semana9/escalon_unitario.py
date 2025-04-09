import numpy as np

def run():
    inputs = np.array([[0,0], [0,1], [1,0],[1,1]])

    targets = np.array([0,1,1,1])

    targets2 = np.array([0,0,0,1])

    weight = np.array([1,1])

    bias = -2

    outputs = []

    for i in range(targets2.shape[0]):
        # np.dot es el calculo del producto punto
        h = np.dot(inputs[i], weight) + bias
        y = escalon(h)
        outputs.append([h,y])

    print("Input1", "Input2", "Comb. Lineal", "Target","Output")

    for i in range(4):
        print(' ',inputs[i][0], '     ', inputs[i][1], '       ', outputs[i][0], '      ',targets2[i], '        ', outputs[i][1])

def escalon(x):
    if x < 0:
        return 0
    else:
        return 1
    
run()