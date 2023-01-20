from tkinter import *

root = Tk()

def changepages(event):
    root2 = Tk()
    frame1= Frame(root2)
    button5 = Button(text="This is button5")
    button5.pack()
    Frame.pack(root2)
    root2.mainloop()


button1 = Button(text="button1", fg="black", bg="green")
button2 = Button(text="button2", fg="black", bg="green")
button3 = Button(text="button3", fg="black", bg="green", command=changepages)
button4 = Button(text="button4", fg="black", bg="green", command=root.quit)

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)

root.mainloop()
