# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()

# set the pen and fill colors
painter.pencolor('red')
painter.pensize(10)
painter.fillcolor('yellow')
# then draw a circle
painter.begin_fill()
painter.circle(100)
painter.end_fill()

# move the turtle to another part of the screen
painter.penup()
painter.goto(0,-200)
painter.pendown()

# change both the pen and fill colors
# then draw a polygon of your choice
painter.pencolor('purple')
painter.fillcolor('blue')
painter.begin_fill()
painter.circle(100,steps=5)
painter.end_fill()

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()
