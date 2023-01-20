from tkinter import *

root = Tk()
#binding fuction to a widget

def printName(event):
    print('heloo my name is jorden')

def leftclick(event):
    print('left')
def middleclick(event):
    print('middle')
def rightclick(event):
    print('right')

button = Button(root, text='Print name',)
button.bind("<Button-1>", printName)
button.bind('<Button-3>', rightclick)
button.pack()

#defining clicks
frame = Frame(root, width=600, height=400)


frame = Frame(root, width=600, height=400)
frame.bind('<Button-1>', leftclick)
frame.bind('<Button-2>',middleclick)
frame.bind('<Button-3>',rightclick)
frame.pack()
#it starts here



root.mainloop()
