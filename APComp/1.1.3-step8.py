"""
Ben Campbell 9/7/22
1.1.13 Step 8
Draw a circle with for loop
"""

import turtle as trtl

#Turtle object and set shape
painter = trtl.Turtle()
painter.shape("circle")

#Loop 18 times, move forward 20 pixels, left 20 degrees, and stamp turtle at each vertex
for x in range(18):
    painter.forward(20)
    painter.stamp()
    painter.left(20)

painter.penup()
painter.goto(0, -100)
painter.pendown()

#Draw octogon with while loop
count = 0
while count < 8:
    painter.forward(30)
    painter.left(360/8)
    count += 1

#Keep program open till user provides an input
input()
