import numpy as np
import sys

#Numpy Array is contiguous and occupy less memory
def main():
    #NumPy Array
    arr = np.array([10, 56, 65, 98, 90])
    print(f'Array in numpy : {arr}')     
    print(f'Type : {type(arr)}')
    print(arr.nbytes)   #bytes of array

    #Python List
    python_list = [12, 67, 86, 43, 23]
    print(f'List : {python_list}')
    print(f'Type : {type(python_list)}')
    print(sys.getsizeof(python_list[0])*len(python_list))  #Python List memory is fragmented
if __name__ == '__main__':
    main()
