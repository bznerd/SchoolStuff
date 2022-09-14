"""
Ben Campbell 9/14/22
1.1.5 Mazes 1-3
Robot navigates 3 different mazes
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

def reset():
    robot.goto(startx, starty)

def color_change():


#------ maze paths
maze1 = [[4, move], [3, turn_left], [4, move]]
maze2 = [[3, move], [3, turn_left], [2, move], [1, reset], [3, turn_left], [3, move], [1, turn_left]]
maze3 = [[1, move], [3, turn_left], [2, move], [1, turn_left], [1, move]]

mazes = {"1": (maze1, "maze1.png"), "2": (maze2, "maze2.png"), "3": (maze3, "maze3.png")}

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


maze = '' 
while True:
    maze = input("What maze should be run? ")
    if maze in mazes:
        maze = mazes[maze]
        break
    else: print("Please enter a valid maze number")


wn.bgpic(maze[1])# other file names should be maze2.png, maze3.png

for step in maze[0]:
    for x in range(step[0]):
        step[1]()

wn.mainloop()
