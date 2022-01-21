from tkinter.constants import HORIZONTAL
from normalization import date_transform, normalize
from daily_script import columns_add, english_check, add_open_int
from monthly_script import english_check_of_month, period_create, saving_months
from quarter_script import quarter_period_create, english_check_of_quarter, quarter_saving
from saving import txt_convert
from tkinter import Label, Tk
from tkinter.ttk import Progressbar
from time import sleep



def extract(path, output, case):
    qmd = case[:1]
    extract_window = Tk()
    extract_window.title('Konwersja...')
    extract_window.geometry('400x200')
    label = Label(extract_window, text='Start konwersji')
    label.pack(pady=30)
    percent_label = Label(extract_window, text=f'0%')
    percent_label.pack()
    progress = Progressbar(extract_window, orient = HORIZONTAL,
              length = 100, mode = 'determinate')  
    progress.pack(pady=40)

    def refresh_counter(num: int):
        percent_label.config(text=f'{num}%')

    def start():
        progress['value'] = 0
        extract_window.update_idletasks()
        if qmd == 'd':
            label.config(text='Normalizuje dane')
            normalized_data = normalize(path, case)
            progress['value'] = 10
            refresh_counter(progress['value'])
            extract_window.update_idletasks()
            dates = date_transform(normalized_data)
            progress['value'] = 25
            refresh_counter(progress['value'])
            extract_window.update_idletasks()
            label.config(text='Zmieniam kolumny')
            eng = english_check(dates)
            progress['value'] = 45
            refresh_counter(progress['value'])
            extract_window.update_idletasks()
            label.config(text='Tworze data frame')
            cols = columns_add(eng)
            progress['value'] = 67
            refresh_counter(progress['value'])
            extract_window.update_idletasks()
            label.config(text='Dodaje wykres OPEN_INT')
            open_int = add_open_int(cols, 'nonpath')
            print(open_int)
            progress['value'] = 85
            refresh_counter(progress['value'])
            extract_window.update_idletasks()
            label.config(text='Konwertuje do pliku .txt')
            txt_convert(open_int, path, output, 'D')
            label.config(text='Zakończono!')
            progress['value'] = 100
            refresh_counter(progress['value'])
            extract_window.update_idletasks()
            sleep(0.4)
            extract_window.destroy()

        if qmd == 'm':
            label.config(text='Normalizuje dane')
            normalized_data = normalize(path,case)
            progress['value'] = 17
            refresh_counter(progress['value'])
            extract_window.update_idletasks()
            dates = date_transform(normalized_data)
            progress['value'] = 34
            refresh_counter(progress['value'])
            extract_window.update_idletasks()
            label.config(text='Zmieniam nazwy kolumn')
            eng = english_check_of_month(dates)
            progress['value'] = 51
            refresh_counter(progress['value'])
            extract_window.update_idletasks()
            label.config(text='Wytwarzam okresy')
            periods = period_create(eng)
            progress['value'] = 68
            refresh_counter(progress['value'])
            extract_window.update_idletasks()
            label.config(text='Zapisuje okresy')
            data_to_df = saving_months(eng, periods)
            progress['value'] = 85
            refresh_counter(progress['value'])
            extract_window.update_idletasks()
            label.config(text='Konwertuje do pliku .txt')
            txt_convert(data_to_df, path, output, 'D')
            label.config(text='Zakończono!')
            progress['value'] = 100
            refresh_counter(progress['value'])
            extract_window.update_idletasks()
            sleep(0.4)
            extract_window.destroy()
        if qmd == 'q':
            label.config(text='Normalizuje dane')
            normalized_data = normalize(path,case)
            progress['value'] = 17
            refresh_counter(progress['value'])
            extract_window.update_idletasks()
            dates = date_transform(normalized_data)
            progress['value'] = 34
            refresh_counter(progress['value'])
            extract_window.update_idletasks()
            label.config(text='Sprawdzam kwartały')
            eng = english_check_of_quarter(dates)
            progress['value'] = 51
            refresh_counter(progress['value'])
            extract_window.update_idletasks()
            label.config(text='Tworze okresy kwartalne')
            periods = quarter_period_create(eng)
            progress['value'] = 68
            refresh_counter(progress['value'])
            extract_window.update_idletasks()
            label.config(text='Zapisuje kwartały do pamięci')
            data_to_df = quarter_saving(eng, periods)
            progress['value'] = 85
            refresh_counter(progress['value'])
            extract_window.update_idletasks()
            label.config(text='Zapisuje do pliku .txt')
            txt_convert(data_to_df, path, output, 'D')
            progress['value'] = 100
            refresh_counter(progress['value'])
            extract_window.update_idletasks()
            sleep(0.4)
            extract_window.destroy()

    extract_window.after(10, start)
    extract_window.mainloop()



# # extract('/Users/marianpazdzioch/Downloads/wse stocks/prm.txt', '/Users/marianpazdzioch/Desktop/rolowania', 'qtxt')
# # extract('/Users/marianpazdzioch/Downloads/wse stocks/prm.txt', '/Users/marianpazdzioch/Desktop/rolowania', 'mtxt')
# extract('/Users/marianpazdzioch/Desktop/konwerter_kwartalny/eurpln_d.csv', '/Users/marianpazdzioch/Desktop/konwerter_kwartalny', 'dcsv')
# # extract('/Users/marianpazdzioch/Desktop/konwerter_kwartalny/eurpln_d.csv', '/Users/marianpazdzioch/Desktop/rolowania', 'mcsv')

