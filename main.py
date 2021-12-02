# -*- coding: utf-8 -*-
from quarter_script import quarter_script
from daily_script import daily_script
from version import version_window
from tkinter import *
from tkinter import filedialog
import sys
import os

f = open('version.txt', 'r')
content = f.read()

class State():
    path = None
    output = None
    filename = None
    done = False
    version = "0.2.1"


state = State

def reset():
    state.path = None
    state.output = None
    state.filename = None
    state.done = False

def error_label(error):
    label = Label(root, text=error)
    label.pack()
    label.place(relx=0.5,rely=0.2,anchor=CENTER)

def path_label(path):
    label = Label(root, text=path)
    label.pack()
    label.place(relx=0.2,rely=0.33,anchor=CENTER)

def output_label(path):
    label = Label(root, text=path)
    label.pack()
    label.place(relx=0.6,rely=0.33,anchor=CENTER)

def filename_label(filename):
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

def start_conversion_of_quarter():
    try:
        quarter_script(state.path, state.output)
    except:
        if state.path is None or state.output is None:
            if state.path is None:
                error_label("Brak pliku")
            if state.output is None:
                error_label("Brak ściezki wyjścia")
            if state.path is None and state.output is None:
                error_label("Brak atrybutów (nazwa pliku, ścieka wyjścia)")

def start_conversion_of_daily():
    try:
        daily_script(state.path, state.output)
    except:
        if state.path is None or state.output is None:
            if state.path is None:
                error_label("Brak pliku")
            if state.output is None:
                error_label("Brak ściezki wyjścia")
            if state.path is None and state.output is None:
                error_label("Brak atrybutów (nazwa pliku, ścieka wyjścia)")

def version():
    version_window(root, content)

root = Tk()
root.title('Konwerter kwartałów v{}'.format(state.version))
root.geometry('600x400')


if state.done is True:
    label = Label(root, text="Zakonczono konwersje kwartału")
    label.pack()
    label.place(relx=0.5,rely=0.8,anchor=CENTER)
    state.reset()

button = Button(root, text="Wybierz plik", command=choose_file_path)
button.pack()
button.place(relx=0.5,rely=0.38,anchor=CENTER)

button = Button(root, text="Wybierz ściezkę wyjścia", command=get_output)
button.pack()
button.place(relx=0.5,rely=0.46,anchor=CENTER)

button = Button(root, text="Konwertuj kwartalnie", command=start_conversion_of_quarter)
button.pack()
button.place(relx=0.5,rely=0.54,anchor=CENTER)

button = Button(root, text="Konwertuj dziennie (OPEN_INT)", command=start_conversion_of_daily)
button.pack()
button.place(relx=0.5,rely=0.62,anchor=CENTER)

button = Button(root, text="Wyjdź", command=exit)
button.pack()
button.place(relx=0.5,rely=0.70,anchor=CENTER)

button = Button(root, text="Wersja", command=version)
button.pack()
button.place(relx=0.9,rely=0.9,anchor=CENTER)


root.mainloop()