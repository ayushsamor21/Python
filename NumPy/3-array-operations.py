import numpy as np

def main():
    arr = np.array([[35, 17, 10], [89, 6, 77]], dtype=float)
    print(np.sort(arr))
    print((np.sort(arr, axis=None)))  #array in one dimension

    empty_array = np.zeros((3, 4))    #empty array with each element's value 0
    print(empty_array)

    array2 = np.ones((3, 3))    #matrix with each element value 1
    print(array2)

    #Range in NumPy
    range_array = np.arange(10)
    print(range_array)

    range_array2 = np.arange(5, 20)
    print(range_array2)

    range_array3 = np.arange(20, 40, 2)
    print(range_array3)

    #linearly spaced
    range_array4 = np.linspace(10, 20, 5) #linspace(start, stop, num) by default it is 50
    print(range_array4)

    #Array in 1-dimension for overview
    print(np.ravel(arr))   #np.flatten(arr) can also be used

    print(arr.reshape(3, 2))   #the number of elements should be same

    #MAX IN ARRAY
    print(arr.max())
    print(np.max(arr))

    #MIN IN ARRAY
    print(arr.min())
    print(np.min(arr))

    #SUM OF ROWS : AXIS = 1
    print(arr.sum(axis = 1))

    #SUM OF COLUMNS : AXIS = 0
    print(arr.sum(axis = 0))

if __name__ == '__main__':
    main()
