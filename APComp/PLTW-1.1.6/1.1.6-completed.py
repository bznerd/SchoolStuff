"""
Ben Campbell 9/16/22
1.1.6 Completed bug
Draws ladybug
"""

import turtle as trtl

#Ladybug turtle object
ladybug = trtl.Turtle()

# config dots
dot_size = 10
relative_dots = [(15,10), (-13,-10), (20,-18), (-21, 14)]
origin = (0,-35)

#Define parameters to be mirrored on each side
legs = 3
leg_range = 45
leg_len = 60
offset = (0,-35)
leg_size = 7


#For both sides draw the number of legs radiating outward
ladybug.pensize(leg_size)
for x in range(2):
    side = 0 if x == 0 else 180
    for y in range(legs):
        ladybug.penup()
        ladybug.goto(offset)
        ladybug.seth(side - (1/2 * leg_range) + (y * leg_range/(legs-1)))
        ladybug.pendown()
        ladybug.forward(leg_len)

#Reset position for head
ladybug.penup()
ladybug.goto(0,0)
ladybug.seth(0)
ladybug.pendown()

# create ladybug head
ladybug.pensize(40)
ladybug.circle(5)

# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# draw two sets of dots
ladybug.pensize(dot_size)
for dot in relative_dots:
  ladybug.penup()
  ladybug.goto(map(lambda a,b: a+b, dot, origin)) 
  ladybug.pendown()
  ladybug.circle(3)

#Hide turtle at end
ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()
