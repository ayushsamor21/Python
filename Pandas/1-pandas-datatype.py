import pandas as pd
import numpy as np

def main():
    #dict : dictionary
    dataset = {
       'NAME' : ['ayush ', 'rajveer', 'rudra'],
       'marks': [23, 78, 90]
    }

    #<class 'pandas.core.frame.DataFrame'>
    data = pd.DataFrame(dataset, index=[1, 2, 3])
    print(data)

    #Series
    arr = np.array([1, 2, 3])

    data2 = pd.Series(arr, index = ['x', 'y', 'z'])
    print(data2)
    print(data2['y'])

    #key value objects using dictionary
    dataset2 = {"ayush" : 95, "rajveer" : 91, "rudra": 89}

    data3 = pd.Series(dataset2)
    print(data3)

if __name__ == '__main__':
    main()
