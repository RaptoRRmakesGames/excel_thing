import pandas as pd 
import sys 


def main():
    
    df = pd.DataFrame({'Part Number':[], 'Part Description':[], 'Quantity':[], 'Unit':[]})
        
    df.to_excel("file.xlsx", index=False)
    
    with open("items.txt", "w") as f:
        f.write("")


if __name__ == "__main__":
    main() 
    sys.exit()