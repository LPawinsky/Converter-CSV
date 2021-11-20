from main_script import script
from tkinter import *
from tkinter import filedialog
import sys
import os

class State():
    path = None
    output = None


state = State

def exit():
    sys.exit(root)

def choose_file_path():
    file_path = filedialog.askopenfilename(filetypes=[('DANE CSV','.csv')])
    state.path = file_path
    print(state.path)

def get_output():
    output_path = filedialog.askdirectory()
    state.output = output_path
    print(state.output)

def start_conversion():
    if not (state.path is None) and not (state.output is None):
        head, tail = os.path.split(state.path)
        filename = tail
        script(state.path, state.output, filename)


root = Tk()
root.title('Konwerter kwartałów')
root.geometry('800x600')

button = Button(root, text="Wybierz plik", command=choose_file_path)
button.pack()
button.place(relx=0.5,rely=0.42,anchor=CENTER)

button = Button(root, text="Wybierz ściezkę wyjścia", command=get_output)
button.pack()
button.place(relx=0.5,rely=0.46,anchor=CENTER)

button = Button(root, text="Konwertuj", command=start_conversion)
button.pack()
button.place(relx=0.5,rely=0.5,anchor=CENTER)

button = Button(root, text="Wyjdź", command=exit)
button.pack()
button.place(relx=0.5,rely=0.54,anchor=CENTER)


root.mainloop()