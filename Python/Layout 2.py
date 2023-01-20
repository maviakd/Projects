from tkinter import *

root = Tk()
root.geometry('200x100')

def horz():
    print("Horizontal pairs")

def vert():
    print("Vertical pairs")

button1 = Button(root, text="T", fg="white",bg="black", command=vert)
button1.pack(fill=X)

button2 = Button(text="R", fg="white",bg="black", command = vert)
button2.bind("<Button-1>")
button2.pack(side=RIGHT, fill=Y)

button3 = Button(text="L", fg="white", bg="black", command = horz)
button2.bind("<Button-1>")
button3.pack(side=LEFT, fill=Y)

button4 = Button(text="B", fg="white",bg="black", command = vert)
button4.bind("<Button-1>")
button4.pack(side=BOTTOM, fill=X)



root.mainloop()
