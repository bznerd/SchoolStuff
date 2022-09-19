"""
Ben Campbell 9/19/22
1.1.7 Step 17
List of turtles that draw a spiral with different shapes and colors
"""

import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold"]

#Assign colors, shapes, and penup to each new color
for s in turtle_shapes:
    t = trtl.Turtle(shape=s)
    t.color(turtle_colors.pop())
    t.penup()
    my_turtles.append(t)

#Variables that give position for a turtle before it begins its moves and distance to move
start = (0,0)
heading = 90
move = 50

#Loop through list of turtles and run commands for each
for t in my_turtles:
    t.goto(start)
    t.seth(heading)
    t.pendown()
    t.right(45)		 
    t.forward(move)

    #Save current turtle state for starting point of next turtle and increment forward movement distance
    start = t.pos()
    heading = t.heading()
    move += 5

wn = trtl.Screen()
wn.mainloop()
