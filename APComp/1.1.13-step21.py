"""
Ben Campbell 9/7/22
1.1.13 Step 21
Draw three towers with three colors alternating every three floors
"""

import turtle as trtl

#Setup turtle object as painter
painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150
colors = ["gray", "purple", "blue"]

# height of tower and a counter for each floor
num_floors = 63

# iterate
for floor in range(num_floors):
    #Move to a location determined by floor number and modulus operations
    painter.penup()
    painter.goto(x + 75*(floor//21), y + 5*(floor%21))
    #set color in a repeating pattern over the list of colors
    painter.color(colors[(floor//3)%len(colors)])
     
    #draw the floor
    painter.pendown()
    painter.forward(50)

#Wait for user input before closing program
input()
