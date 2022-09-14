"""
Ben Campbell 9/14/22
1.1.5 Mazes 1
Robot navigates mazes
"""

import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#Set image to maze1 
wn.bgpic("maze1.png")# other file names should be maze2.png, maze3.png

#Up to top corner
for x in range(4):
    move()

#Turn right (3 lefts)
for x in range(3):
    turn_left()

#Move across top to sqaure
for x in range(4):
    move()

wn.mainloop()
