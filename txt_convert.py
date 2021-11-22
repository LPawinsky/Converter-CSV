import pandas as pd

def txt_convert():
    data = pd.read_csv('/Users/marianpazdzioch/Desktop/program/20211122_dh5.txt')
    df = pd.DataFrame(data)
    print(df)
    

txt_convert()