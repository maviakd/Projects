import turtle
import random
import math
import os

os.system('7, the element.mp3')

speed = 1
speed2 = 1

maxgoals = 5
goals = []

wn = turtle.Screen()
wn.bgcolor('black')
wn.tracer(3)


def turnright():
    player.right(30)

def turnleft():
    player.left(30)

def increasespeed():
    global speed
    speed += 1

def decreasespeed():
    global speed
    speed -= 1

def collision (t1, t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2)) + math.pow(t1.ycor()-t2.ycor(), 2)
    if d < 20:
        global maxgoals
        return True
    else:
        return False



pen = turtle.Turtle()
pen.color('white')
pen.penup()
pen.setposition(-250, -250)
pen.pendown()
pen.pensize(4)
pen.speed(0)
for side in range(4):
    pen.forward(500)
    pen.left(90)
pen.hideturtle()



for count in range(maxgoals):
    goals.append(turtle.Turtle())
    goals[count].shape("circle")
    goals[count].color('green')
    goals[count].penup()
    goals[count].speed(0)




player = turtle.Turtle()
player.shape('triangle')
player.color('white')
player.penup()
player.speed(0)
player.setposition(random.randint(-240, 240), random.randint(-240, 240))



turtle.listen()
turtle.onkey(turnleft, 'Left')
turtle.onkey(turnright, 'Right')
turtle.onkey(increasespeed, 'Up')
turtle.onkey(decreasespeed, 'Down')

while True:
    goals[count].forward(speed2)
    player.forward(speed)

    if player.xcor() > 240 or player.xcor() < -240:
        player.left(180)
    if player.ycor() > 240 or player.ycor() < -240:
        player.left(180)

    for count in range(maxgoals):
        goals[count].forward(3)
        if goals[count].xcor() > 240 or goals[count].xcor() < -240:
            goals[count].left(180)

        if goals[count].ycor() > 240 or goals[count].ycor() < -240:
            goals[count].left(180)

        if collision(goals[count], player):
            goals[count].right(random.randint(0, 360))
            goals[count].hideturtle()
            goals[count].setposition(random.randint(-240, 240), random.randint(-240, 240))
            goals[count].showturtle()
