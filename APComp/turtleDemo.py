"""
Ben Campbell
8/30/22
Turtle basics
"""
import math
dis_down = math.sqrt(3)/2 * 100
import turtle
t = turtle.Turtle()
t.pensize(width = 5)
t.pencolor('purple')
t.penup()
t.goto(-100,(-1/2)*dis_down)
t.pendown()

for x in range(3):
    t.forward(200)
    t.left(120)

t.penup()
t.forward(100)
t.left(60)
t.pendown()

for x in range(3):
    t.forward(100)
    t.left(120)

t.penup()
t.goto(0,-300)


width = 200
height = 200
diag = (40,40)

def drawline(startx, starty, endx, endy):
    t.penup()
    t.goto(startx,starty)
    t.pendown()
    t.goto(endx, endy)
    t.penup()

drawline(0,-300, 0, -300+height)
drawline(width,-300, width, -300+height)
drawline(diag[0],-300+diag[1], diag[0], -300+height+diag[1])
drawline(diag[0]+width,-300+diag[1], diag[0]+width, -300+height+diag[1])

drawline(0,-300,0+width,-300)
drawline(0,-300+height,0+width,-300+height)
drawline(0+diag[0], -300+diag[1], 0+width+diag[0], -300+diag[1])
drawline(0+diag[0], -300+diag[1]+height, 0+width+diag[0], -300+height+diag[1])

drawline(0,-300, 0+diag[0], -300+diag[1])
drawline(0,-300+height, 0+diag[0], -300+diag[1]+height)
drawline(0+width,-300, 0+diag[0]+width, -300+diag[1])
drawline(0+width,-300+height, 0+diag[0]+width, -300+diag[1]+height)

t.goto(400,100)
t.pendown()
t.pencolor('yellow')
t.circle(100)
t.penup()
t.goto(400-100,180)
t.pendown()
t.pencolor('blue')
t.begin_fill()
t.circle(20)
t.end_fill()
t.penup()
t.goto(400-20, 180)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()
t.penup()
t.goto(400-120, 120)
t.seth(t.heading()-90)
t.pendown()
t.pencolor('red')
t.circle(100, extent=60)

input()
