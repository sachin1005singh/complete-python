from turtle import *
color('red','blue')
begin_fill()
while True:
    speed(14)
    forward(200)
    lt(170)
    if abs(pos())< 1:
        break
    
end_fill()
done()
