from pandas import date_range, DatetimeIndex, DataFrame, to_datetime

def columns_add(data):
    if 'Vol' not in sorted(data):
        data['Vol'] = 0
    if 'Vol' in sorted(data):
        data['OpenInt'] = 0
        return data

def indices_of_dates(df,third_fridays, case):
    indices = []
    for f in third_fridays:
        f = f.strftime('%Y-%m-%d')
    for date in df['Date']:
        index = df.index
        if date in third_fridays:
            condition = df['Date'] == date
            index_date = index[condition]
            indices.append(index_date)
    return indices

def add_open_int(df, case):
    third_fridays = date_range(df['Date'].iloc[len(df.index)-len(df.index)], df['Date'].iloc[len(df.index)-1], freq='WOM-3FRI')
    indices = indices_of_dates(df,third_fridays, case)
    for i in indices:
        date = df['Date'].iloc[i]
        date = to_datetime(date)
        month = DatetimeIndex([date]).month_name()
        if month[0] == 'March' or month[0] == 'June' or month[0] == 'September' or month[0] == 'December':
            df.at[i, 'OpenInt'] = 3
        else:
            df.at[i, 'OpenInt'] = 1
    return df


def english_check(data):
    if sorted(data)[0] == 'Data':
        df = DataFrame(data, columns=['Data','Najwyzszy', 'Najnizszy','Otwarcie','Zamkniecie'])
        df = df.rename({'Najwyzszy':'High', 'Najnizszy':'Low', 'Otwarcie':'Open', 'Zamkniecie':'Close', 'Data':'Date',}, axis='columns')
        return df
    if sorted(data)[0] != 'Data':
        return data
