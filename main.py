from tkinter import filedialog, Label, Button, Tk
from tkinter.constants import ACTIVE, CENTER
from State import State
from version import version_window
import os

state = State(None, None, '0.6')

def version_button_action():
    version_window()

def path_button_action():
    filetypes = (('Pliki .csv .txt', '.csv .txt'))
    file_path = filedialog.askopenfilename(title='Otwórz', filetypes=filetypes)
    state.update_path(str(file_path))
    path_label()

def output_button_action():
    output_path = filedialog.askdirectory()
    state.update_output(str(output_path))
    output_label()

def exit_button_action():
    import sys
    sys.exit(root)


def quarter_roll_button_action():
    from Validate import Validate
    validate = Validate(state.path, state.output_path, 'Q')
    validate.validation()

def monthly_roll_button_action():
    from Validate import Validate
    validate = Validate(state.path, state.output_path, 'M')
    validate.validation()

def daily_roll_button_action():
    from Validate import Validate
    validate = Validate(state.path, state.output_path, 'D')
    validate.validation()

def path_label():
    label = Label(root, text='Obiekt konwersji:')
    label.pack()
    label.place(relx=0.2,rely=0.20,anchor=CENTER)
    label = Label(root, text=os.path.basename(os.path.normpath(state.path)))
    label.pack()
    label.place(relx=0.2,rely=0.25,anchor=CENTER)

def output_label():
    label = Label(root, text="Konwersja do:")
    label.pack()
    label.place(relx=0.8,rely=0.20,anchor=CENTER)
    label = Label(root, text=['/',os.path.basename(os.path.normpath(state.output_path))])
    label.pack()
    label.place(relx=0.8,rely=0.25,anchor=CENTER)


root = Tk()
root.geometry('600x400')
root.title(f'Konwerter kontraktów v{state.version}')

path_button = Button(root, text='Wybierz plik', command=path_button_action)
path_button.pack()
path_button.place(relx=0.5,rely=0.3,anchor=CENTER)

output_button = Button(root, text='Wybierz ściezkę wyjścia', command=output_button_action)
output_button.pack()
output_button.place(relx=0.5,rely=0.37,anchor=CENTER)



quarter_roll_button = Button(root, text='Wykres kontraktów kwartału', command=quarter_roll_button_action)
quarter_roll_button.pack()
quarter_roll_button.place(relx=0.5,rely=0.5,anchor=CENTER)
quarter_roll_button.configure(state=ACTIVE)
monthly_roll_button = Button(root, text='Wykres kontraktów miesiąca', command=monthly_roll_button_action)
monthly_roll_button.pack()
monthly_roll_button.place(relx=0.5,rely=0.57,anchor=CENTER)
monthly_roll_button.configure(state=ACTIVE)
daily_roll_button = Button(root, text='Wykres kontraktów dzienny (OPEN_INT)', command=daily_roll_button_action)
daily_roll_button.pack()
daily_roll_button.place(relx=0.5,rely=0.64,anchor=CENTER)
daily_roll_button.configure(state=ACTIVE)

exit_button = Button(root, height=1, width=20, text='Wyjdź', command=exit_button_action)
exit_button.pack()
exit_button.place(relx=0.5,rely=0.8,anchor=CENTER)
exit_button.configure(state=ACTIVE)

version_button = Button(root, text='Wersja', command=version_button_action)
version_button.pack()
version_button.place(relx=0.9,rely=0.9,anchor=CENTER)
version_button.configure(state=ACTIVE)



root.mainloop()

