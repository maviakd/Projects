from tkinter import *
import tkinter.messagebox

answer = tkinter.messagebox.askquestion("hi", "do you want to start this program")

if answer == "yes":
    root = Tk()

    def donothing():
        print("this is the command")

    menu = Menu(root)
    root.config(menu=menu)
    import tkinter.messagebox


    submenu = Menu(menu)

    menu.add_cascade(label="file", menu=submenu)
    submenu.add_cascade(label="new project", command=donothing)
    submenu.add_cascade(label="new...", command= donothing)
    submenu.add_separator()
    submenu.add_cascade(label="exit", command=root.quit)

    submenu2=Menu(menu)

    menu.add_cascade(label="edit", menu=submenu2)
    submenu2.add_cascade(label="edit1", command=donothing)
    submenu2.add_cascade(label="edit2", command=donothing)
    submenu2.add_cascade(label='edit3', command=donothing)

    status = Label(root, text="this is the status meter", bd=1, relief=SUNKEN, anchor=W)
    status.pack(side=BOTTOM, fill=X)

    root.mainloop()