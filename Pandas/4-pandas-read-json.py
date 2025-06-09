import pandas as pd

def main():
    df = pd.read_json('json_dataset.json')
    print(df)

    #Entire dataFrame
    print(df.to_string())
    
    print(pd.options.display.max_rows)

if __name__ == '__main__':
    main()
