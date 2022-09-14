"""
Ben Campbell 9/8/22
1.1.3 Step 17
Draw a flower with three rings of pedals each different colors
"""

import turtle as trtl
import math

#Move to correct location and stamp a petal
def drawPedal(ring, index, center, petals=18):
    painter.penup()
    ringSize = 20 + int(35 * ring)
    angle = index * ((2*math.pi)/petals) + (1/2 * math.pi)
    petalCoords = (ringSize * math.cos(angle) + center[0], ringSize * math.sin(angle) + center[1])
    painter.goto(petalCoords)
    painter.stamp()

painter = trtl.Turtle()
painter.speed(0)

# stem
painter.color("green")
painter.pensize(15)
painter.goto(0, -150)
painter.setheading(90)
painter.forward(100)
#  leaf
painter.setheading(270)
painter.circle(20, 120, 20)
painter.setheading(90)
painter.goto(0, -60)
# rest of stem
painter.forward(60)
painter.setheading(0)

# change pen
painter.penup()
painter.shape("circle")
painter.turtlesize(2)


#Iterate through three rings every four pedals in a ring the color changes
#For each ring iterate 18 pedals stamped by the turtle
colors = ['blue', 'red', 'purple','yellow']
for ring in range(3):
  painter.goto(0-(5*(ring+1)),130+(13*ring**2))
  for petal in range(18):
    flower_index = 22*ring + petal
    painter.color(colors[(flower_index//4)%4])
    drawPedal(ring, petal, (0,110))

#Wait for keyboard input to close program
input()
