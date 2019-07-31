import turtle
import math,random
import os

wn = turtle.Screen() #setup screen
wn.bgcolor("black")
wn.bgpic("Capture.png")
wn.title("Welcome to BubbleShort Game")
wn.tracer(3)

#draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-270,-270)
mypen.pendown()
mypen.pensize(3)

for side in range(4):
    mypen.color("white")
    mypen.forward(540)
    mypen.left(90)
mypen.hideturtle()


player = turtle.Turtle()
player.color("green")
player.shape("turtle")
player.penup()
player.speed(0)
player.shapesize(2)

#create the score variable
score = 0

#create goal
mygoal  = 10
goals =[]
for count in range(mygoal):

    goals.append(turtle.Turtle())
    goals[count].color("red")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-260,260) , random.randint(-60,260))
    
speed = 1 #set speed

# defing function

def turnleft():
    player.left(30)

def turnright():
    player.right(30)



# for speed

def increasespeed():
    global speed
    speed += 1

def decreasespeed():
    global speed
    speed -= 1

# is collision

def iscollision(t1,t2):
     d = math.sqrt(math.pow(t1.xcor()- t2.xcor(),2)) + math.pow(t1.ycor()-t2.ycor(),2)
     if d <20:
        return True
     else:
        return False

    
        
#set key binding

turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed , "Up")
turtle.onkey(decreasespeed, "Down")

while True:
    player.forward(speed)



    #boundary checking
    if player.xcor() > 270 or player.xcor() < -270:
        player.right(70)
        
    
    if player.ycor() > 270 or player.ycor() < -270:
        player.right(70)
        
        
   
    #move the goal
    for  count in range(mygoal):
        
        goals[count].forward(3)    
            

          #boundary checking  
        if goals[count].xcor() > 260 or goals[count].xcor() < -260:
            goals[count].right(100)
            
            

        
        if goals[count].ycor() > 260 or goals[count].ycor() < -260:
            goals[count].right(100)
            
            

         #collision checking
        #d = math.sqrt(math.pow(player.xcor()- goal.xcor(),2)) + math.pow(player.ycor()-goal.ycor(),2)
        if iscollision(player,goals[count]):
            goals[count].setposition(random.randint(-270,270) , random.randint(-270,270))
            goals[count].right(random.randint(0,360))
            os.system("afplay music1.mp3&")
            score  += 1
            #draw the score in screen
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-255,270)
            scorestring = "Score : %r" %score
            mypen.write(scorestring, False , align = "left" , font = ("",14, "normal"))
            print(score)

         

        #goal.hideturtle()






delay = input("Press Enter to finish.")
