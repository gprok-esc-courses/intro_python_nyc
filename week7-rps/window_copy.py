
from tkinter import Tk, Button, Label, Entry, Frame

def button_clicked():
    name = entry.get()
    label.config(text="Hello " + name)

window = Tk()
window.geometry("400x300")
window.title("My First Window")

f1 = Frame(window)
f2 = Frame(window)
f3 = Frame(window)
label = Label(f1, text="-")
button = Button(f2, text="Click Me", command=button_clicked)
entry = Entry(f3)


# label.grid(row=0, column=1)
# entry.grid(row=1, column=1)
# button.grid(row=2, column=1)
f1.pack()
label.pack()
f2.pack()
button.pack()
f3.pack()
entry.pack()

window.mainloop()