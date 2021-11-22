import pandas as pd
import os
import re

def create_all_columns(df):
    df.columns = df.columns.str.upper()
    df = df.assign(TICKER = 0, PER = 'D', TIME = '000000')
    df = df[['TICKER', 'PER', 'DATE','TIME', 'OPEN', 'HIGHEST', 'LOWEST', 'CLOSE', 'VOLUME', 'OPENINT']]
    return df

def format_col_names(df):
    df = df.rename({'TICKER':'<TICKER>','PER':'<PER>','DATE':'<DATE>','TIME':'<TIME>','OPEN':'<OPEN>','HIGHEST':'<HIGH>','LOWEST':'<LOW>','CLOSE':'<CLOSE>','VOLUME':'<VOL>','OPENINT':'<OPENINT>'}, axis='columns')
    return df

def filename_for_ticker(path):
    filename = os.path.basename(path)
    filename = re.sub('[!@#$_-]', '', filename)
    filename2 = filename
    filename2 = filename2[:-5]
    return filename2

def ticker(df, filename):
    df['<TICKER>'] = filename.upper()
    return df

def date_formatting(df):
    df['<DATE>'] = pd.to_datetime(df['<DATE>'])
    df['<DATE>'] = df['<DATE>'].dt.strftime('%Y%m%d')
    return df

def output(df):
    df = pd.DataFrame(df)
    df.to_csv('output.txt', index=False)

def txt_convert(data, path):
    df_with_all_cols = create_all_columns(data)
    formatted_cols = format_col_names(df_with_all_cols)
    filename = filename_for_ticker(path)
    df_with_ticker = ticker(formatted_cols, filename)
    formatted_date_df = date_formatting(df_with_ticker)
    output(formatted_date_df)