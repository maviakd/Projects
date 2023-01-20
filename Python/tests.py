import turtle
import random

class Restaurant(object):
    bankrupt = False
    def open_branch(self):
        if not self.bankrupt:
            print("branch opened")

class ClassNames:
    def CreateNames (self,name):
        self.name=name
    def Printname(self):
        return self.name
    def SayName(self):
        print("hello %s" % self.name)

class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def changelocation(self):
    # I haven't programmed it to spawn outside the snake's body yet
    self.x = random.randint(0, 20)*20 - 200
    self.y = random.randint(0, 20)*20 - 200

first = ClassNames()
first.CreateNames("Chris")
first.Printname()
first.SayName()