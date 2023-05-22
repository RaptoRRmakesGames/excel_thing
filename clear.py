import pandas as pd
import sys

def main():
    df = pd.read_excel("file.xlsx")
    
    for i in range(len(df)):
        df = df.drop(i)

    df.to_excel("file.xlsx", index=False)

if __name__ == '__main__':
    main()
    sys.exit()