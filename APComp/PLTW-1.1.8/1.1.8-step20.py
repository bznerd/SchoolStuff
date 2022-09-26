"""
Ben Campbell 9/22/22
1.1.8 Step 20
Turtles move until they collide
"""

import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

step_size = 6 
collision_dis = 20 

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:
    # Initialize Turtle, add it too hroizontal list, move it to location, set color and heading
    ht = trtl.Turtle(shape=s)
    horiz_turtles.append(ht)
    ht.penup()
    new_color = horiz_colors.pop()
    ht.fillcolor(new_color)
    ht.goto(-350, tloc)
    ht.setheading(0)

    # Same as above but with vertical
    vt = trtl.Turtle(shape=s)
    vert_turtles.append(vt)
    vt.penup()
    new_color = vert_colors.pop()
    vt.fillcolor(new_color)
    vt.goto( -tloc, 350)
    vt.setheading(270)
    
    #Increment location variable
    tloc += 50

# 50 movement steps for the turtles
for step in range(50):
    #For every turtle in the lists move, or remove
    for turtle in range(len(horiz_turtles)):
        # Get the horizontal and vertical turtles from the lists
        ht = horiz_turtles[turtle]
        vt = vert_turtles[turtle]
        
        # If the x and y coords are within the specified collision distance, remove them from the lists (effectively stops their movement), otherwise they move a step
        if abs(vt.xcor()-ht.xcor()) > collision_dis and abs(vt.ycor()-ht.ycor()) > collision_dis:
            ht.forward(step_size)
            vt.forward(step_size)

        else:
            horiz_turtles.remove(ht)
            vert_turtles.remove(vt)

wn = trtl.Screen()
wn.mainloop()
