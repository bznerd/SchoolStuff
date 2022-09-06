"""
Ben Campbell 9/6/2022
AP Comp 2nd 
Basic turtle drawing of a laptop
"""

# import turtle module
import turtle as trtl
import math

# create turtle object
painter = trtl.Turtle()

#Basic parameters for sizing
width = 150
height = 80
offset = 10
screen_color = input("What Screen Color Would you like?")

#Convert degrees to radians
def toRad(degrees):
    return (degrees/360)*(2*math.pi)

#Very primitive parallelogram draw procedure
def parallelgram(width, height, angle):
    painter.forward(width)
    painter.left(180- angle)
    painter.forward(height)
    painter.left(angle)
    painter.forward(width)
    painter.left(180-angle)
    painter.forward(height)
    painter.left(angle)

painter.pensize(3)

#Draw lower half
painter.fillcolor('black')
painter.begin_fill()
parallelgram(width, height, 80)
painter.end_fill()
painter.penup()
painter.goto(math.cos(toRad(100))*80, math.sin(toRad(100))*80)
painter.pendown()

#Draw upper half
painter.fillcolor('black')
painter.begin_fill()
parallelgram(width, height, 90)
painter.end_fill()
painter.penup()
painter.goto(painter.pos()+(5,5))
painter.pendown()

#Draw screen bezel
painter.fillcolor(screen_color)
painter.begin_fill()
parallelgram(width-10, height-10, 90)
painter.end_fill()
painter.penup()
painter.goto(3, 30)
painter.pendown()

#Draw keyboard
painter.fillcolor('gray')
painter.begin_fill()
parallelgram(width - (2*offset), 42, 80)
painter.end_fill()
painter.penup()
painter.goto(55, 5)
painter.pendown()

#Draw trackpad
painter.fillcolor('gray')
painter.begin_fill()
parallelgram(35,20, 80)
painter.end_fill()

#Don't close program imidiately
input()
