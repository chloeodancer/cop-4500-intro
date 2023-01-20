import numpy as np
def array_function():
    array1 = np.array(([0, 0, 0], [0, 0, 0], [0, 0, 0]))
    for i in range(0, 3):
        for j in range(0, 3):
            if i==j:
                array1[i][j] = 1
            else:
                array1[i][j] = 0

    print(array1)
    print ("\n")

    for i in range(0, 3):
        for j in range(0,3):
            if i == j:
                array1[i][j] = 1
            else:
                array1[i][j] = 3
    print(array1)
    print("\n")

    array1 = np.delete(array1, 2, 1)
    print(array1)

if __name__ == "__main__":
    array_function()

