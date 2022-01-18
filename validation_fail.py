def validation_fail(msg: str):
    def exit():
        window.destroy()
    import tkinter as tk
    from tkinter.constants import CENTER
    window = tk.Tk()
    window.title('Błąd')
    window.geometry('300x150')

    label = tk.Label(window, text=msg)
    label.pack()
    label.place(relx=0.5,rely=0.33,anchor=CENTER)
    ok = tk.Button(window, text='OK', command=exit)
    ok.pack()
    ok.place(relx=0.5, rely=0.66, anchor=CENTER)
    window.mainloop()