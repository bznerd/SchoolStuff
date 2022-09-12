"""
Ben Campbell 9/8/22
1.1.3 Step 17
Draw a flower with three rings of pedals each different colors
"""

import turtle as trtl

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

# draw flower
painter.goto(20,180)


#Iterate through three rings every four pedals in a ring the color changes
#For each ring iterate 18 pedals stamped by the turtle
colors = ['blue', 'red', 'purple','yellow']
for ring in range(3):
  painter.goto(0-(5*(ring+1)),130+(13*ring**2))
  for petal in range(18):
    flower_index = 22*ring + petal
    painter.forward(10*(ring+1))
    painter.right(20)
    painter.color(colors[(flower_index//4)%4])
    painter.stamp()
