import numpy as np

def main():
    arr = np.array([1, 3, 5])
    print(arr)
    print(f'Dimension : {arr.ndim}')

    #Multi dimensional array
    arr2 = np.array([[1, 3, 6], [9, 6, 7]], dtype=float)  #data type can be specified within the array
    print(arr2)
    print(f'Data Type of Array: {arr2.dtype}')
    print(f'Dimension of Array: {arr2.ndim}')
    print(f'The shape of Array : {arr2.shape}')  #(2,3)
    print(f'Bytes : {arr2.nbytes}')
    print(f'Each Element Byte : {arr2.itemsize}')
    print(f'Number of elements : {arr2.size}')

if __name__ == '__main__':
    main()
