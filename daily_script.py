import pandas as pd
from txt_convert import txt_convert

def columns_add(data):
    if 'Vol' not in sorted(data):
        data['Vol'] = 0
    if 'Vol' in sorted(data):
        data['OpenInt'] = 0
        return data

def indices_of_dates(df,third_fridays, case):
    indices = []
    for date in df['Date']:
        if case == 'nonpath':
            date = date.strftime("%Y-%m-%d")
        for friday in third_fridays:
            if date == friday.strftime("%Y-%m-%d"):
                index = df.index[df['Date'] == friday.strftime("%Y-%m-%d")]
                indices.append(index)
    return indices

def add_open_int(df, case):
    third_fridays = pd.date_range(df['Date'].iloc[len(df.index)-len(df.index)], df['Date'].iloc[len(df.index)-1], freq='WOM-3FRI')
    indices = indices_of_dates(df,third_fridays, case)
    for i in indices:
        date = df['Date'].iloc[i]
        month = pd.DatetimeIndex(date).month_name()
        if month[0] == 'March' or month[0] == 'June' or month[0] == 'September' or month[0] == 'December':
            df.at[i, 'OpenInt'] = 3
        else:
            df.at[i, 'OpenInt'] = 1
    return df

def english_check(data):
    if sorted(data)[0] == 'Data':
        df = pd.DataFrame(data, columns=['Data','Najwyzszy', 'Najnizszy','Otwarcie','Zamkniecie'])
        df = df.rename({'Najwyzszy':'High', 'Najnizszy':'Low', 'Otwarcie':'Open', 'Zamkniecie':'Close', 'Data':'Date',}, axis='columns')
        return df
    if sorted(data)[0] != 'Data':
        return data

def daily_script(path, output, path_data, case):
    data = None
    if case == 'path':
        data = pd.read_csv(path)
    if case == 'nonpath':
        data = path_data
    df = pd.DataFrame(data)

    with_all_columns = columns_add(english_check(df))
    correct_dataframe_with_periods = add_open_int(with_all_columns, case)
    txt_convert(correct_dataframe_with_periods, path, output, 'D')

# daily_script('/Users/marianpazdzioch/Downloads/wse stocks/4fm.txt', '/Users/marianpazdzioch/Desktop')
