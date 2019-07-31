import turtle
from turtle import *

"""
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("yellow")

tess.penup()                # This is new
size = 15
for i in range(36):
   tess.stamp()             # Leave an impression on the canvas
   size = size + 3          # Increase the size on every iteration
   tess.forward(size)       # Move tess along
   tess.right(25)           #  ...  and turn her


turtle.reset()




"""
from turtle import *
colors = ['#78B3DB', '#F238AD', '#38F2BA', '#EBF238', '#F25D38', '#38DFF2']
for x in range(360):
    pensize(1)
    bgcolor("black")
    speed(0)
    pencolor(colors[x % 6])
    width(x / 100 + 1)
    forward(x)
    left(91)

turtle.clearscreen()

# Python program to draw 
# Rainbow Benzene
# using Turtle Programming
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(300):
    t.speed(0)
    t.pencolor(colors[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)
