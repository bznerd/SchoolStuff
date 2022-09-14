"""
Ben Campbell 9/14/22
1.1.5 Mazes 3
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


#Set image to maze3
wn.bgpic("maze3.png")# other file names should be maze2.png, maze3.png

#Same path to first square and second square
for x in range(2):
    #Loop 4 move turn iterations per step to square
    for y in range(4):
        move()
        #On even iterations turn right, on odd turn left
        for z in range(3-(2*(y%2))):
            turn_left()

    #Change pencolor to green after first movement iteration
    robot.pencolor('green')

wn.mainloop()
