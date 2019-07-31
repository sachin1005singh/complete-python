import turtle
from turtle import *
star = turtle.Turtle()
bgcolor("black")
star.color("blue")
star.setpos(-50,300)
star.write("shape of star ", True, font = ("arial",20,"bold"))
star.home()
for i in range(50):

    star.pensize(1)
    star.speed(10)
    star.forward(i*10)
    star.right(144)

turtle.clearscreen()
turtle.reset()


#2nd figure
turtle.reset()
turtle.ht()
bgcolor("black")
begin_fill()
painter = turtle.Turtle()
painter.pencolor("blue")
painter.hideturtle()
painter.setpos(-550, -20)
for i in range(50):
    
    painter.speed(0)
    painter.forward(150)
    painter.left(123)

painter.pencolor("red")
for i in range(70):
    painter.fd(280)
    painter.left(123)

painter.setpos(-50,300)
painter.write("use of circle  ", True, font = ("arial",20,"bold"))

end_fill()


turtle.reset()

# 3rd figure

ninja = turtle.Turtle()
ninja.color("yellow")
ninja.speed(0)
ninja.pensize(1)
ninja.hideturtle()
ninja.shape("circle")
ninja.shapesize(2)

for i in range(180):
    ninja.fd(120)
    ninja.right(30)
    ninja.fd(20)
    ninja.left(70)
    ninja.forward(60)
    ninja.right(40)

    ninja.penup()
    ninja.setposition(0,0)
    ninja.pendown()

    ninja.right(2)


# 4th figure repeat
turtle.reset()
turtle.ht()
begin_fill()
painter = turtle.Turtle()
painter.pencolor("blue")
painter.hideturtle()
painter.setpos(300, 20)
for i in range(50):
    
    painter.speed(0)
    painter.forward(150)
    painter.left(123)

painter.pencolor("red")
for i in range(70):
    painter.fd(280)
    painter.left(123)



turtle.clearscreen()


# fifth figure
cir  = Turtle()

cir.screen.bgcolor("black")
cir.setpos(50,300)
cir.write("color of National Flag ", True, font = ("arial",20,"bold"))
cir.home()

colors = [ "orange", "white" ,  "green"]
for x in range(120):
   cir.speed(0)
   cir.circle(x)
   cir.color(colors[x%3])
   cir.left(60)


turtle.clearscreen()


# 6th figure
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("white")

tess.penup()            
size = 15
for i in range(30):
   tess.stamp()            
   size = size + 3          
   tess.forward(size)       
   tess.right(25)       


turtle.reset()

# combine figure


for i in range(400):
    turtle.ht()# this "for" loop will repeat these functions 500 times
    bgcolor("black")
    color("blue")
    speed("fastest")
    forward(i)

    left(91)

turtle.reset()

turtle.clearscreen()
 # 8th figure
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


turtle.done()


