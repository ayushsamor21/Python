import numpy as np
from numpy.random import standard_t

def main():
    arr = np.array([[3, 6, 1], [6, 7, 3]])

    for rows in arr:
        print(f'rows-> {rows}')

    #SQUARE
    square = np.square(arr)
    print(square)

    #SQUARE ROOT
    square_root = np.sqrt(arr)
    print(square_root)

    #STANDARD DEVIATION
    print(np.std(arr))

if __name__ == '__main__':
    main()
