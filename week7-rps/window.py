
from tkinter import Tk, Button, Label, Entry

def button_clicked():
    name = entry.get()
    label.config(text="Hello " + name)

window = Tk()
window.geometry("400x300")
window.title("My First Window")


label = Label(window, text="-")
button = Button(window, text="Click Me", command=button_clicked)
entry = Entry(window)

label.grid(row=0, column=1)
entry.grid(row=1, column=1)
button.grid(row=2, column=1)


window.mainloop()