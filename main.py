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
    file_path = filedialog.askopenfilename(filetypes=[('Dane CSV (.csv)','.csv')])
    state.path = file_path
    print(state.path)

def get_output():
    output_path = filedialog.askdirectory()
    state.output = output_path
    print(state.output)

def start_conversion():
    try:
        head, tail = os.path.split(state.path)
        filename = tail
        script(state.path, state.output, filename)
    except:
        print('Błąd')

    # if not (state.path is None) and not (state.output is None):
    #     head, tail = os.path.split(state.path)
    #     filename = tail
    #     script(state.path, state.output, filename)
    
    # if state.path is None and state.output is None:
    #     print(f"Brak atrybutów: ściezka CSV - {state.path} lub ściezka zapisu - {state.output}")


root = Tk()
root.title('Konwerter kwartałów')
root.geometry('800x600')

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