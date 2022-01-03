from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from version import version_window
from Decider import Decider
from State import State
import os
import sys

state = State('0.3.1', None, None, None, 0)
root = Tk()

def error_label(error):
    label = Label(root, text=error)
    label.pack()
    label.place(relx=0.5,rely=0.15,anchor=CENTER)

def exit_system():
    sys.exit(root)

# decider functions

def trigger_decider(case):
    decider = Decider(case,str(state.path),str(state.output))
    if state.path == None:
        error_label('Brak ściezki pliku')
    if state.path != None:
        if state.output == None:
            error_label('Brak wyjścia końcowego')
        if state.output != None:
            decider.case_decide()


# button actions

def open_int_button_action():
    trigger_decider('D')

def quarter_button_action():
    trigger_decider('Q')


# files and outputs

def choose_file_path():
    file_path = filedialog.askopenfilename(filetypes=[('Dane (.csv)','.csv .txt')])
    head, tail = os.path.split(str(state.path))
    state.update_path(str(file_path))
    state.update_filename(tail)
    print(state.path, state.filename)
    path_label()

def get_output():
    output_path = filedialog.askdirectory()
    state.update_output(output_path)
    print(state.output)
    output_label()


# functions to write taken parameters, communication labels


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
    label = Label(root, text=['/',os.path.basename(os.path.normpath(state.output))])
    label.pack()
    label.place(relx=0.8,rely=0.25,anchor=CENTER)


# main program


root.title('Konwerter kwartałów v{}'.format(state.getVersion()))
root.geometry('600x400')

file_path_button = Button(root, text="Wybierz plik", command=choose_file_path)
file_path_button.pack()
file_path_button.place(relx=0.5,rely=0.38,anchor=CENTER)
file_path_button.configure(state=ACTIVE)

output_path_button = Button(root, text="Wybierz ściezkę wyjścia", command=get_output)
output_path_button.pack()
output_path_button.place(relx=0.5,rely=0.46,anchor=CENTER)
output_path_button.configure(state=ACTIVE)

quarter_button = Button(root, text="Konwertuj kwartalnie", command=quarter_button_action)
quarter_button.pack()
quarter_button.place(relx=0.5,rely=0.54,anchor=CENTER)
quarter_button.configure(state=ACTIVE)

open_int_button = Button(root, text="Konwertuj dziennie (OPEN_INT)", command=open_int_button_action)
open_int_button.pack()
open_int_button.place(relx=0.5,rely=0.62,anchor=CENTER)
open_int_button.configure(state=ACTIVE)

exit_button = Button(root, text="Wyjdź", command=exit_system)
exit_button.pack()
exit_button.place(relx=0.5,rely=0.70,anchor=CENTER)

version_button = Button(root, text="Wersja", command=version_window)
version_button.pack()
version_button.place(relx=0.9,rely=0.9,anchor=CENTER)
version_button.configure(state=ACTIVE)



root.mainloop()
