import pandas as pd
from datetime import datetime

def date_transform(df):
    df['Date'] = pd.to_datetime(df['Date'].astype(str), format='%Y-%m-%d')
    return df

def renames(data):
    df = pd.DataFrame(data, columns=['<DATE>','<OPEN>','<HIGH>','<LOW>','<CLOSE>'])
    df.rename(columns={'<DATE>':'Date','<OPEN>':'Open','<HIGH>':'High','<LOW>':'Low','<CLOSE>':'Close'}, inplace=True)
    return df

def convert_data(path):
    data = pd.read_csv(path)
    df = renames(data)
    transformed_df = date_transform(df)
    return transformed_df
