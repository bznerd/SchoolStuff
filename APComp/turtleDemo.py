"""
Ben Campbell
8/30/22
Turtle basics
"""

import turtle
t = turtle.Turtle()
t.pensize(width = 5)
t.begin_fill()

#for color in ['red', 'green', 'blue', 'yellow']:
#    t.color(color)
#    t.forward(75)
#    t.left(90)

t.setheading(-1*(360/16))
t.color('red')
t.circle(100, steps=8)
t.fillcolor('red')
t.end_fill()
t.penup()
t.sety(50)
t.color('white')
t.write("STOP")


input()
