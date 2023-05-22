import pandas as pd
import sys

# dataframe.head(num) gives 'num' amount of results. Default is 5
# dataframe.shape() gives tuple. first item is how many rows and second is how many collumns
# .<collumn_name> returns only the collumn with that name

deb = False

def debug(item):
    global deb
    
    if deb:
        print(item)

def main():

    # Read the xlsx to create a dataframe 

    file_frame = pd.read_excel("file.xlsx")

    # collect all the lines from the txt file

    with open("items.txt", "r") as f : 
        
        textlines = f.readlines()
        textlines = [item.strip("\n")  for item in textlines ]
        
        for line in textlines:
            if len(line) < 5:
                textlines.remove(line)

    debug(textlines) 

    for line in textlines:
        new_ln = line.split()
        new_ln[0] = "'"+new_ln[0]
        print(new_ln)
        
        while True:
            try: 
                
                file_frame.loc[len(file_frame)] = new_ln
                break
            
            except ValueError:
                
                ln = new_ln

                new_ln = [ln[0], ln[1] + " " + ln[2], ln[3], ln[4]]
                
                try:
                    for i in range(5, 200):
                        new_ln.append(ln[i])
                    
                except IndexError:
                    pass
        
    # correct types
    
    for i in file_frame.loc[0:len(file_frame), "Part Number"]:
        i = str(i)
        #debug(f"{i}, {type(i)}")
        
    for i in file_frame.loc[0:len(file_frame), "Quantity"]:
        i = float(i)
        #debug(f"{i}, {type(i)}")
        
    debug(file_frame)
    
    # file_frame = file_frame.reset_index().rename(columns={'index': 'ln'})

    file_frame.to_excel("file.xlsx", index = False)
    
    if not deb:
        with open("items.txt", "w") as f:
            f.write("")

if __name__ == "__main__": 
    main()
    sys.exit()