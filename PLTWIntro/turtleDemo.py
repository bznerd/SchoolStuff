import turtle
import math

window = turtle.Screen()
myTurtle = turtle.Turtle()



def drawSquare(x=0, y=0, color="black", size=100, fillSize=1, startHeading=0):
    myTurtle.penup()
    myTurtle.goto(x,y)
    myTurtle.pencolor(color)
    myTurtle.pensize(fillSize)
    myTurtle.pendown()
    for x in range(4):
        myTurtle.setheading(90*x + startHeading)
        myTurtle.forward(size)

drawSquare(y=-137.5, color="orange", size=200, fillSize=100, startHeading=45)

for x in range(4):
    myTurtle.penup()
    myTurtle.goto(math.cos(x*math.pi/2)*math.sqrt(2000)/2, math.sin(x*math.pi/2)*math.sqrt(2000)/2)
    myTurtle.pendown()
    myTurtle.color("blue")
    myTurtle.circle(25)

myTurtle.penup()
myTurtle.goto(0,0)

myTurtle.shape('square')

window.exitonclick()