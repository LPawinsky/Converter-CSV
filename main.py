from main_script import script
from tkinter import *
from tkinter import filedialog
import sys
import os

class State():
    path = None
    output = None
    filename = None
    done = False
    version = "0.1"


state = State

def reset():
    state.path = None
    state.output = None
    state.filename = None
    state.done = False

def error_label(error: str) -> str:
    label = Label(root, text=error)
    label.pack()
    label.place(relx=0.5,rely=0.2,anchor=CENTER)

def path_label(path: str) -> str:
    label = Label(root, text=path)
    label.pack()
    label.place(relx=0.2,rely=0.33,anchor=CENTER)

def output_label(path: str) -> str:
    label = Label(root, text=path)
    label.pack()
    label.place(relx=0.6,rely=0.33,anchor=CENTER)

def filename_label(filename: str) -> str:
    label = Label(root, text=filename)
    label.pack()
    label.place(relx=0.5,rely=0.3,anchor=CENTER)

def exit():
    sys.exit(root)

def choose_file_path():
    file_path = filedialog.askopenfilename(filetypes=[('Dane CSV (.csv)','.csv')])
    state.path = file_path
    head, tail = os.path.split(state.path)
    state.filename = tail
    path_label(state.path)
    filename_label(state.filename)

def get_output():
    output_path = filedialog.askdirectory()
    state.output = output_path
    output_label(state.output)

def start_conversion():
    try:
        script(state.path, state.output, state.filename)
    except:
        if state.path is None or state.output is None:
            if state.path is None:
                error_label("Brak pliku")
            if state.output is None:
                error_label("Brak ściezki wyjścia")
            if state.path is None and state.output is None:
                error_label("Brak atrybutów")

root = Tk()
root.title(f'Konwerter kwartałów v{state.version}')
root.geometry('600x400')


if state.done is True:
    label = Label(root, text="Zakonczono konwersje kwartału")
    label.pack()
    label.place(relx=0.5,rely=0.8,anchor=CENTER)
    state.reset()

button = Button(root, text="Wybierz plik", command=choose_file_path)
button.pack()
button.place(relx=0.5,rely=0.40,anchor=CENTER)

button = Button(root, text="Wybierz ściezkę wyjścia", command=get_output)
button.pack()
button.place(relx=0.5,rely=0.50,anchor=CENTER)

button = Button(root, text="Konwertuj", command=start_conversion)
button.pack()
button.place(relx=0.5,rely=0.60,anchor=CENTER)

button = Button(root, text="Wyjdź", command=exit)
button.pack()
button.place(relx=0.5,rely=0.70,anchor=CENTER)


root.mainloop()