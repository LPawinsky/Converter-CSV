from datetime import timedelta
from pandas import date_range, to_datetime
from normalization import normalize, date_transform


data_to_df = []

def weekly_periods(df):
    periods = []
    fridays = date_range(df['Date'].iloc[len(df.index)-len(df.index)], df['Date'].iloc[len(df.index)-1], freq='W-FRI')
    starting_days_array = []
    ending_days_array = []
    for i in fridays:
        starting_day = i + timedelta(days=3)
        ending_days_array.append(i)
        starting_days_array.append(starting_day)
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
    try:
        df['Date'] = to_datetime(df['Date'])
        startDay = to_datetime(startDay)
        endDay = to_datetime(endDay)
        after_date = df['Date'] >= startDay
        before_date = df['Date'] <= endDay
        between = after_date & before_date
        filtered_dates = df.loc[between]
        highest_price = filtered_dates['High'].max()
        lowest_price = filtered_dates['Low'].min()
        opening_price = filtered_dates["Open"].iloc[len(filtered_dates.index)-len(filtered_dates.index)]
        closing_price = filtered_dates['Close'].iloc[len(filtered_dates.index)-1]
        return startDay, endDay, highest_price, lowest_price, opening_price, closing_price
    except:
        return None

def write_single_period(data):
    data_to_df.append([data[1], data[4], data[2], data[3], data[5], 0, 0])

def weekly_saving(df, periods):
    for i in range(0, len(periods), 2):
        if i < len(periods)-1:
            s = to_datetime(periods[i].to_datetime64())
            e = to_datetime(periods[i+1].to_datetime64())
            s = s.date()
            e = e.date()
            data = get_prices_of_period(df, s, e)
            if data != None:
                write_single_period(data)
        if i == len(periods) - 1:
            s = to_datetime(periods[i].to_datetime64())
            s = s.date()
            try:
                e = to_datetime(periods[i+1].to_datetime64())
                e = e.date()
                data = get_prices_of_period(df, s, e)
                write_single_period(data)
                break
            except:
                max = df['Date'].max()
                e = max.to_datetime64()
                e = to_datetime(e)
                e = e.date()
                data = get_prices_of_period(df, s, e)
                write_single_period(data)
            finally:
                break

    return data_to_df