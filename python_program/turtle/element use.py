import turtle 
turtle.bgcolor("blue")
turtle.pensize(10)
turtle.color("green", "yellow")
turtle.begin_fill()
turtle.speed(1)
turtle.shape("turtle")
turtle.fd(50)
turtle.circle(70)
turtle.shapesize(5,1)
turtle.settiltangle(90)
turtle.fd(100)
turtle.end_fill()


turtle.shape("square")
turtle.shaptransform(4,-1,0,2)
turtle.get_shapepoly()
turtle.end_fill()


turtle.reset()
turtle.resizemode("auto")
turtle.speed(6)
turtle.shape("triangle")
turtle.tilt(90)
turtle.shaptransform()
turtle.end_fill()
