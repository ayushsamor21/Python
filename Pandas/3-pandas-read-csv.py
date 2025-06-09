import pandas as pd

def main():
    #First and Last 5 rows for large dataframe
    df = pd.read_csv('employee_data.csv')
    print(df)

    #For entire DataFrame
    print(df.to_string())

    #maximum row printing in system
    print(pd.options.display.max_rows)

if __name__ == '__main__':
    main()
