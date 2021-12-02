from tkinter import *

def version_window(root, content):
    content = str(content)
    window = Toplevel(root)
    window.title("Wersja programu")
    window.geometry("400x200")
    Text(window, text=content).pack()
