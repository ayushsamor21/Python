import numpy as np

def main():
    arr1 = np.array([[34, 67, 84], [23, 54, 12], [90, 54, 11]])
    arr2 = np.array([[10, 20, 40], [63, 14, 72], [90, 98, 11]])

    #VECTOR ADDITION  : python list just concatenate list
    arr3 = arr1 + arr2
    print(arr3)

    print(arr3 * 100)

    #DOT PRODUCT
    arr3 = np.array([10, 30, 40])
    arr4 = np.array([90, 10, 60])

    print(np.dot(arr3, arr4))

    #CROSS PRODUCT
    print(np.cross(arr3, arr4))

if __name__ == '__main__':
    main()
