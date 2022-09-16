"""
Ben Campbell 9/15/22
1.1.6 step 31
Debugging with readability, bug fixes, and improvements
"""

import turtle as trtl
import math

#Make turtle and draw a circle for the body
painter = trtl.Turtle()
painter.pensize(40)
painter.circle(20)

#Drawing parameters for legs and eyes
legs = 8
leg_len = 70 
leg_angle_offset = 100 / (legs/2)
eye_size = 5 
eye_spacing = 50
painter.pensize(5)

#Leg drawwing loop
loop_counter = 0
while (loop_counter < legs):
    painter.goto(0,20)
    #drawlegs on opposite side after first 4 itterations
    painter.setheading((180 if loop_counter > 3 else 0) +  leg_angle_offset*(loop_counter%4))
    painter.forward(leg_len)
    loop_counter = loop_counter + 1

#Draw eyes
painter.pencolor('white')
painter.pensize(5)
#Two eyes
for x in range(2):
    painter.penup()
    #Calculate angle using offset to be directly inbetween the sets of legs
    angle = (100 + (180-100)/2) - (eye_spacing/2) + (x * eye_spacing)
    angle *= math.pi / 180
    #Polar coords (radius + angle) to cartesian 
    painter.goto(30*math.cos(angle), 30*math.sin(angle)+20)
    painter.pendown()
    painter.circle(eye_size)


#Finish and show screen
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()
