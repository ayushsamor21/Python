import numpy as np

def main():
    arr = np.array([10, 20, 30, 40])

    #SLICING
    print(arr[0:2]) # 10, 20
    print(arr[2:])  # 30, 40
    print(arr[-1])  # 40
    print(arr[-2:]) # 30, 40

    arr2 = np.array([[10, 20, 30], [70, 90, 40], [30, 10, 20]])

    print(arr2[1, 2])    # Matrix numbering starts from 0

    print(arr2[-1])
    print(arr2[-1, 1:])

    #COLUMN SLICING
    print(arr2[:,1:2])

    #Concatenation
    array1 = np.array([['ayush samor', 16, 90], ['rajveer', 17, 90]])
    array2 = np.array([[1], [2]])
    array3 = np.array(['rahual', 22, 89])

    #Horizontal stack
    array4 = np.hstack((array2,array1))
    print(array4)

    #vertical stack
    array5 = np.vstack((array1, array3))
    print(array5)

    #split horizontal
    print(np.hsplit(array5, [2]))

if __name__ == '__main__':
    main()
