import pandas as pd

def main():
    dataset = {
        'Name' : ['ayush', 'rudra', 'rajveer'],
        'marks' : [96, 43, 90]
    }

    df = pd.DataFrame(dataset, index=[1, 2, 3])
    print(df)

    #indexing
    print(df.loc[[1]])
    print(df.loc[[1, 2]])
    print(df.shape)
    print(df.columns)
    print(df['Name'].unique())

if __name__ == '__main__':
    main()
