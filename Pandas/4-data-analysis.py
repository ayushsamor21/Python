import pandas as pd

def main():
    dataset = pd.read_csv('employee_data.csv')
    print(dataset)

    #By-default : 5
    print(dataset.head(10))
    print(dataset.tail(10))

    #info of the dataset
    print(dataset.info())

if __name__ == '__main__':
    main()
