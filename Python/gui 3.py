from tkinter import*
import turtle


t = turtle.Turtle()
ts = t.getscreen()
t.shape("turtle")
t.color("yellow")
ts.bgcolor("black")

i = 0
go = False

def move():
    global go
    go = not go
    while(go):
        t.forward(2)
ts.onkey(move, "space")

def turn_left():
    t.left(90)
ts.onkey(turn_left, "Left")

def turn_right():
    t.right(90)
ts.onkey(turn_right, "Right")

def spin():
    for i in range(4):
        t.right(90)
ts.onkey(spin, "s")






ts.listen()



ts.mainloop()