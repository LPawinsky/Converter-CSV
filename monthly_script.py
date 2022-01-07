import pandas as pd
import datetime as dt
from quarter_script import get_prices_of_period
from txt_convert import txt_convert

data_to_df = []

def case_check(path, path_data, case):
    if case == 'path':
        return pd.read_csv(path)
    if case == 'nonpath':
        return path_data

def english_check(data):
    if sorted(data)[0] == 'Data':
        df = pd.DataFrame(data, columns=['Data','Najwyzszy', 'Najnizszy','Otwarcie','Zamkniecie','Vol','OpenInt'])
        df = df.rename({'Najwyzszy':'High', 'Najnizszy':'Low', 'Otwarcie':'Open', 'Zamkniecie':'Close', 'Data':'Date',}, axis='columns')
    if sorted(data)[0] != 'Data':
        df = pd.DataFrame(data, columns=['Date', 'High', 'Low', 'Open', 'Close', 'Vol', 'OpenInt'])
    return df

def period_create(df):
    periods = []
    third_fridays = pd.date_range(df['Date'].iloc[len(df.index)-len(df.index)], df['Date'].iloc[len(df.index)-1], freq='WOM-3FRI')
    starting_days_array = []
    ending_days_array = []
    for date in third_fridays:
        date = date + dt.timedelta(days=3)
        starting_days_array.append(date)
    for date in third_fridays:
        ending_days_array.append(date)
    if len(starting_days_array) == len(ending_days_array):
        for index, date in enumerate(starting_days_array):
            ending_days_array_index = len(ending_days_array)-1
            if index < ending_days_array_index:
                periods.append(date)
                periods.append(ending_days_array[index+1])
            if index == ending_days_array_index:
                periods.append(date)
    return periods


def get_prices_of_period(df, startDay, endDay):
    df['Date'] = pd.to_datetime(df['Date'])
    startDay = pd.to_datetime(startDay)
    endDay = pd.to_datetime(endDay)
    after_date = df['Date'] >= startDay
    before_date = df['Date'] <= endDay
    between = after_date & before_date
    filtered_dates = df.loc[between]
    highest_price = filtered_dates['High'].max()
    lowest_price = filtered_dates['Low'].min()
    opening_price = filtered_dates["Open"].iloc[len(filtered_dates.index)-len(filtered_dates.index)]
    closing_price = filtered_dates['Close'].iloc[len(filtered_dates.index)-1]
    return startDay, endDay, highest_price, lowest_price, opening_price, closing_price

def write_single_period(data):
    data_to_df.append([data[1], data[4], data[2], data[3], data[5], 0, 0])

def saving(df, periods):
    for i in range(0, len(periods), 2):
        if i < len(periods)-1:
            s = pd.to_datetime(periods[i].to_datetime64())
            e = pd.to_datetime(periods[i+1].to_datetime64())
            s = s.date()
            e = e.date()
            data = get_prices_of_period(df, s, e)
            write_single_period(data)
        if i == len(periods) - 1:
            s = pd.to_datetime(periods[i].to_datetime64())
            s = s.date()
            try:
                e = pd.to_datetime(periods[i+1].to_datetime64())
                e = e.date()
                data = get_prices_of_period(df, s, e)
                write_single_period(data)
                break
            except:
                max = df['Date'].max()
                e = max.to_datetime64()
                e = pd.to_datetime(e)
                e = e.date()
                data = get_prices_of_period(df, s, e)
                write_single_period(data)
            finally:
                break

    return True

def monthly_script(path, output, path_data, case):
    data = case_check(path, path_data, case)
    english_data = english_check(data)
    df = pd.DataFrame(english_data)
    periods = period_create(df)
    if saving(df, periods) == True:
        df = pd.DataFrame(data_to_df, columns = ['Date', 'Open', 'High', 'Low', 'Close','Vol','OpenInt'])
        txt_convert(df, path, output, 'D')
    



    # for i in range(0, len(periods), 2):
    #     if i < len(periods)-1:
    #         normal_time_start = periods[i].to_datetime64()
    #         normal_time_end = periods[i+1].to_datetime64()
    #         s = pd.to_datetime(normal_time_start)
    #         s = s.date()
    #         e = pd.to_datetime(normal_time_end)
    #         e = e.date()
    #         data = get_prices_of_period(full_data_frame, s.strftime("%Y-%m-%d"), e.strftime("%Y-%m-%d"))
    #         write_single_period(data)
    #     if i == len(periods)-1:
    #         last_index = df['Date'].index[-2]
    #         normal_time_start = periods[i].to_datetime64()
    #         normal_time_end = df['Date'][last_index]
    #         s = pd.to_datetime(normal_time_start)
    #         s = s.date()
    #         e = pd.to_datetime(normal_time_end)
    #         e = e.date()
    #         data = get_prices_of_period(full_data_frame, s.strftime("%Y-%m-%d"), e.strftime("%Y-%m-%d"))
    #         write_single_period(data)
    #     if len(periods) / 2 % 1:
    #         length = len(periods) / 2 - 0.5
    #         if len(data_to_df) == int(length):
    #             create_formatted_df(data_to_df, path, output)
    #     if len(periods) / 2 == len(data_to_df):
    #         print("true")
