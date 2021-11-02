import pandas as pd
import datetime as dt
import calendar

def create_quarters(df):
    df.date = pd.to_datetime(df.Date)
    df['Quarter'] = pd.PeriodIndex(df.date, freq='Q')
    return df

def create_names_from_date(df):
    df.date = pd.to_datetime(df.Date)
    df['Dayname'] = df.date.dt.day_name()
    df['Day'] = pd.DatetimeIndex(df['Date']).day
    df['Month'] = df.date.dt.month_name().str[:3]
    df['Year'] = pd.DatetimeIndex(df['Date']).year
    return df


def period_create(df):
    periods = []
    third_fridays = pd.date_range(df['Date'].iloc[len(df.index)-len(df.index)], df['Date'].iloc[len(df.index)-1], freq='WOM-3FRI')
    starting_days_array = []
    ending_days_array = []
    for date in third_fridays:
        date = date + dt.timedelta(days=3)
        if date.month == 3:
            starting_days_array.append(date)
        if date.month == 6:
            starting_days_array.append(date)
        if date.month == 9:
            starting_days_array.append(date)
        if date.month == 12:
            starting_days_array.append(date)
    for date in third_fridays:
        if date.month == 3:
            ending_days_array.append(date)
        if date.month == 6:
            ending_days_array.append(date)
        if date.month == 9:
            ending_days_array.append(date)
        if date.month == 12:
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
    after_start_date = df["Date"] >= startDay
    before_end_date = df["Date"] <= endDay
    between_two_dates = after_start_date & before_end_date
    filtered_dates = df.loc[between_two_dates]
    highest_price = filtered_dates['Highest'].max()
    lowest_price = filtered_dates['Lowest'].min()
    opening_price = filtered_dates["Open"].iloc[len(filtered_dates.index)-len(filtered_dates.index)]
    closing_price = filtered_dates['Close'].iloc[len(filtered_dates.index)-1]

    print(filtered_dates)
    print('--------------------------------------------------')
    print(f"Czas kontraktu między: {startDay} -> {endDay}")
    print('\/\/\/\/\/\/\/\/')
    print(f"Najwyzsza cena okresu: {highest_price}")
    print(f"Najnizsza cena okresu: {lowest_price}")
    print(f'Otwarcie okresu: {opening_price}')
    print(f'Zamkniecie okresu: {closing_price}')


def main():
    data = pd.read_csv('/Users/marianpazdzioch/Desktop/program/eurusd_d.csv')
    df = pd.DataFrame(data, columns=['Data','Najwyzszy', 'Najnizszy','Otwarcie','Zamkniecie'])
    df = df.rename({'Najwyzszy':'Highest', 'Najnizszy':'Lowest', 'Otwarcie':'Open', 'Zamkniecie':'Close', 'Data':'Date',}, axis='columns')

    quarterDataFrame = create_quarters(df)
    full_data_frame = create_names_from_date(quarterDataFrame)
    periods = period_create(full_data_frame)
    for i in range(0, len(periods), 2):
        if i < len(periods)-1:
            normal_time_start = periods[i].to_datetime64()
            normal_time_end = periods[i+1].to_datetime64()
            s = pd.to_datetime(normal_time_start)
            s = s.date()
            e = pd.to_datetime(normal_time_end)
            e = e.date()
            get_prices_of_period(full_data_frame, s.strftime("%Y-%m-%d"), e.strftime("%Y-%m-%d"))
        if i == len(periods)-1:
            last_index = df['Date'].index[-1]
            normal_time_start = periods[i].to_datetime64()
            normal_time_end = df['Date'][last_index]
            s = pd.to_datetime(normal_time_start)
            s = s.date()
            e = pd.to_datetime(normal_time_end)
            e = e.date()
            get_prices_of_period(full_data_frame, s.strftime("%Y-%m-%d"), e.strftime("%Y-%m-%d"))
        
        
    
main()