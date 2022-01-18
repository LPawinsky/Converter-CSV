from pandas import to_datetime, DataFrame
import os
import re

def create_all_columns(df, param):
    df.columns = df.columns.str.upper()
    df = df.assign(TICKER = 0, PER = param, TIME = '000000')
    df = df[['TICKER', 'PER', 'DATE','TIME', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOL', 'OPENINT']]
    return df

def format_col_names(df):
    df = df.rename({'TICKER':'<TICKER>','PER':'<PER>','DATE':'<DATE>','TIME':'<TIME>','OPEN':'<OPEN>','HIGH':'<HIGH>','LOW':'<LOW>','CLOSE':'<CLOSE>','VOL':'<VOL>','OPENINT':'<OPENINT>'}, axis='columns')
    return df

def filename_for_ticker(path):
    fn = os.path.basename(path)
    fn = re.sub('[!@#$_-].', '', fn)
    filename = fn
    filename = filename[:-4]
    return filename

def ticker(df, filename):
    df['<TICKER>'] = filename.upper()
    return df

def date_formatting(df):
    df['<DATE>'] = to_datetime(df['<DATE>'])
    df['<DATE>'] = df['<DATE>'].dt.strftime('%Y%m%d')
    return df

def output_file(df, output_path, filename):
    df = DataFrame(df)
    df.to_csv(os.path.join(output_path,r'{}.txt'.format(filename)), index=False)


def txt_convert(data, path, output, param):
    df = DataFrame(data, columns=['Date','Open','High','Low','Close','Vol','OpenInt'])
    df_with_all_cols = create_all_columns(df, param)
    formatted_cols = format_col_names(df_with_all_cols)
    filename = filename_for_ticker(path)
    df_with_ticker = ticker(formatted_cols, filename)
    formatted_date_df = date_formatting(df_with_ticker)
    output_file(formatted_date_df, output, filename_for_ticker(path))