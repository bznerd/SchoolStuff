"""
Ben Campbell 10/4/22
PLTW 1.2.4
Turtle escapes maze
"""

import turtle
import math
import random
from time import time

#Start parameters
num_walls = 10
wall_width = 15
wall_color = 'black'
move_keys = {'w': 90, 'a': 180, 's': 270, 'd': 0}

#Setup screen and three turtles to draw maze, draw display at top and maze_runner
wn = turtle.Screen()
wall_draw = turtle.Turtle()
wall_draw.pencolor(wall_color)
wall_draw.hideturtle()
wall_draw.pensize(2)

text_turt = turtle.Turtle()
text_turt.hideturtle()
text_turt.penup()
text_turt.goto(0, num_walls*wall_width*2 + 20)


maze_runner = turtle.Turtle(shape='circle')
maze_runner.width(1)
maze_runner.pencolor('red')

#Move the turtle when a key is pressed (configured in move_keys)
def move_key_handler(key, turt):
    turt.seth(move_keys[key])
    turt.forward(1)

#Generate a pair of points for a door and barrier randomly
def get_door_barrier(wall_len, width):
    door_barrier = [-1,-1]
    if wall_len > 3*width:
        door_barrier[0] = random.randint(5, wall_len-5)

    if wall_len > 5*width:
        door_barrier[1] =  random.randint(2*width, wall_len - 2*width)

    if door_barrier[1] != -1 and door_barrier[1] >= door_barrier[0] and door_barrier[1] <= door_barrier[0]+width:
        return get_door_barrier(wall_len, width)

    return door_barrier

#Draw the walls of the maze
def draw_walls(walls, width, turt):
    turt.penup()
    turt.goto(0,0)
    turt.pendown()
    #Draw 4 sides for each number of walls 
    for x in range(walls*4):
        #Get door and barrier coords
        door, barrier = get_door_barrier((x+1) * width, width)
        #If a door is speicified and it's not an outer wall draw the wall with a break in it
        if door != -1 and x < (walls-1)*4:
            turt.pendown()
            turt.forward(door)
            turt.penup()
            turt.forward(2*width)
            turt.pendown()
            turt.forward((x * width) - door - width)

        #If it is an outer wall or no door is specified draw an unbroken wall
        else: 
            turt.pendown()
            turt.forward((x+1) * width)
        
        #If a barrier is specified and it's not the last two walls draw a barrier along the wall
        if barrier != -1 and x < walls*4-2:
            turt.penup()
            turt.backward((x+1) * width - barrier)
            turt.left(90)
            turt.pendown()
            turt.forward(2*width)
            turt.backward(2*width)
            turt.right(90)
            turt.penup()
            turt.forward((x+1) * width - barrier)
        turt.left(90)

#Restart routine clears screen, resets maze_runner and timer
def restart():
    maze_runner.clear()
    maze_runner.penup()
    maze_runner.goto(0,0)
    maze_runner.pendown()
    wn.ontimer(lambda: draw_text(time()), 100)

#Draw game instructions and time remaining
def draw_text(game_time):
    text_turt.clear()
    wn.tracer(False)
    if not finished(): 
        text_turt.write(f"Press r to restart the game\nGame time: {round(time() - game_time, 2)} seconds", align='center')
        wn.ontimer(lambda: draw_text(game_time), 100)
    else: text_turt.write(f"Game completed in {round(time() - game_time,2)}seconds\nPress r to restart the game", align='center')
    wn.update()
    wn.tracer(True)


#Check if the maze_runner has left the maze
def finished():
    x_bounds = (num_walls*wall_width*-2, num_walls*wall_width*2 - wall_width)
    y_bounds = ((num_walls-1)*wall_width*-2, x_bounds[0]*-1)
    if maze_runner.xcor() > x_bounds[1] or maze_runner.xcor() < x_bounds[0]: return True
    if maze_runner.ycor() > y_bounds[1] or maze_runner.ycor() < y_bounds[0]: return True
    return False


#Draw walls and start key listners
wn.tracer(False)
draw_walls(num_walls, wall_width, wall_draw)
wn.update()
wn.onkeypress(restart, 'r')
for key in move_keys:
    wn.onkeypress(lambda n=key: move_key_handler(n, maze_runner), key)

#Start the loops
wn.tracer(True)
wn.listen()
restart()

wn.mainloop()
