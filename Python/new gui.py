from tkinter import *
import tkinter.messagebox

root = Tk()

def gui():
    label1 = Label(text="username")
    label2 = Label(text="password")
    global entry1, entry2
    entry1 = Entry()
    entry2 = Entry()

    checkbox = Checkbutton(text="keep me logged in")
    checkbox.grid(row=2, columnspan=3)

    label1.grid(row=0)
    label2.grid(row=1)

    entry1.grid(row=0, column=1)
    entry2.grid(row=1, column=1)

    button1 = Button(text="button1", fg="black", bg="green", command=checking)
    button1.grid(row = 3, columnspan = 3)

    root.mainloop()

def checking():
    x = entry1.get()
    y = entry2.get()

    if x.lower() == 'one' and y == 'two':
        print("Success")
        Root2()
    else:
        answer = tkinter.messagebox.showinfo("Error", f"Credentials : {x} {y}\nNot recognized")


gui()