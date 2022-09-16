"""
Ben Campbell 9/15/22
1.1.6 step 21
Debugging with good names
"""

import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
#Make turtle and draw a circle
painter = trtl.Turtle()
painter.pensize(40)
painter.circle(20)

#Drawing parameters
legs = 6
leg_len = 70 
leg_angle_offset = 380 / legs
painter.pensize(5)

#Leg drawwing loop
loop_counter = 0
while (loop_counter < legs):
  painter.goto(0,0)
  painter.setheading(leg_angle_offset*loop_counter)
  painter.forward(leg_len)
  loop_counter = loop_counter + 1

#Finish and show screen
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()
