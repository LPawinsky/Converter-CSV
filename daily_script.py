from pandas import date_range, DatetimeIndex, DataFrame, to_datetime
import pandas as pd

def columns_add(data):
    if 'Vol' not in sorted(data):
        data['Vol'] = 0
    if 'Vol' in sorted(data):
        data['OpenInt'] = 0
        return data

def convert_third_fridays(third_fridays):
    new_third_fridays = []
    for friday in third_fridays:
        new_third_fridays.append(friday.date())
    return new_third_fridays

def indices_of_dates(df,third_fridays, case):
    indices = []
    fridays = convert_third_fridays(third_fridays)
    for date in df['Date']:
        index = df.index
        if date in fridays:
            condition = df['Date'] == date
            index_date = index[condition]
            indices.append(index_date)
    return indices

def add_open_int(df, case):
    third_fridays = date_range(df['Date'].iloc[len(df.index)-len(df.index)], df['Date'].iloc[len(df.index)-1], freq='WOM-3FRI')
    indices = indices_of_dates(df,third_fridays, case)
    for i in indices:
        date = pd.to_datetime(df['Date'].iloc[i])
        month = date.dt.month
        if month.item() == 3 or month.item() == 6 or month.item() == 9 or month.item() == 12:
            df.loc[i, 'OpenInt'] = 3
        else:
            df.loc[i, 'OpenInt'] = 1
    return df


def english_check(data):
    if sorted(data)[0] == 'Data':
        df = DataFrame(data, columns=['Data','Najwyzszy', 'Najnizszy','Otwarcie','Zamkniecie'])
        df = df.rename({'Najwyzszy':'High', 'Najnizszy':'Low', 'Otwarcie':'Open', 'Zamkniecie':'Close', 'Data':'Date',}, axis='columns')
        return df
    if sorted(data)[0] != 'Data':
        return data
