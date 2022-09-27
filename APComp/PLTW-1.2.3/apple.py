"""
Ben Campbell 9/26/22
Activity 1.2.3
Apples fall from tree when their letters are pressed
"""

import turtle as trtl
import random as rand
from time import time

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

#Text and tree configs
text = ('Arial', 15, 'normal')
tree_wh = (9*40, 200)
tree_center = (0,100)
rowsize = 9
ground_y = -180


#Make and randomize letters and apple positions lists
letters = list("abcdefghijklmnopqrstuvwxyz")
rand.shuffle(letters)
positions = list(range(26))
rand.shuffle(positions)

#Queue of turtles to be displayed
turtle_queue = []

#Configure window
wn = trtl.Screen()
#wn.setup(width=1.0, height=1.0)
wn.bgpic("background.gif")
wn.addshape(apple_image) # Make the screen aware of the new file

#Configure typer to draw letters
typer = trtl.Turtle()
typer.penup()
typer.hideturtle()
typer.color("white")

#-----functions-----
#Vector addition function
def add(*coords):
    total = [0 for x in range(len(coords[0]))]
    for pair in coords:
       total = [total[x] + pair[x] for x in range(len(total))] 
    return tuple(total)


#Convert an index into x,y coords on tree and move turtle
def grid_position(index, turtle): 
    x_spacing = tree_wh[0]/rowsize
    y_spacing = tree_wh[1]/(26//rowsize + 1)
    index = positions[index]
    pos = ((index%rowsize)*x_spacing - (tree_wh[0]/2), (index//rowsize)*y_spacing - (tree_wh[1]/2))
    turtle.goto(add(pos, tree_center))


#Draw letter with a turtle at given location
def draw_letter(turtle, loc, letter):
    turtle.goto(add(loc, (0,-30)))
    turtle.write(letter, align="center", font=text)


#Iterate through letter list and bind turtles
def gen_apples(turtle_queue, letters):
    wn.tracer(False)
    for x, letter in enumerate(letters):
        #Temp turtle var to confgure turtle
        temp_turt = trtl.Turtle(shape=apple_image)
        temp_turt.hideturtle()
        temp_turt.penup()
        temp_turt.seth(270)
        grid_position(x, temp_turt)
        #Add to list
        turtle_queue.append(temp_turt)
    wn.update()


#Business logic side of dropping an apple (graphics split for performance)
def drop_apple_logic(letter, turtle_queue, letters):
    if letter not in letters: return
    index = letters.index(letter)
    letters.pop(index)
    wn.onkeypress(None, letter)
    return turtle_queue.pop(index)


#Graphics side of dorpping an apple
def drop_apple_move(turtle):
    turtle.speed(4)
    turtle.forward(turtle.ycor()-ground_y)
    turtle.hideturtle()


#Draw apples with their letters from the queue (draws only the first five at a time)
def draw_apples(turtle_queue, letters):
    typer.clear()
    if len(letters) > 5: num = 5
    else: num = len(letters)
    for x in range(num):
        turtle_queue[x].showturtle()
        draw_letter(typer, turtle_queue[x].pos(), letters[x].upper())


#Update queue when a key is pressed
def update_queue(letter, turtle_queue, letters):
    #Drop apple
    temp = drop_apple_logic(letter, turtle_queue, letters)
    draw_apples(turtle_queue, letters)
    #Draw apple drop
    wn.update()
    wn.tracer(True)
    pause_listners(letters)
    drop_apple_move(temp)
    wn.tracer(False)
    #Update game status and event listners
    if len(letters) == 0: return game_over()
    event_listeners(turtle_queue, letters)
    

#Generate key listeners
def event_listeners(turtle_queue, letters):
    for key in letters[:5]:
        wn.onkeypress(lambda n=key: update_queue(n, turtle_queue, letters), key)
    

#Unbind all key listners
def pause_listners(letters):
    for key in letters:
        wn.onkeypress(None, key)


#Dispaly game over time
def game_over():
    typer.clear()
    typer.goto(0,0)
    typer.write(f"Game over! Completd in {round(time() - game_time, 1)} seconds", align="center", font=text)


#-----function calls-----
#Initialize the game
gen_apples(turtle_queue, letters)
draw_apples(turtle_queue, letters)
wn.update()

#Start timer and listeners
game_time = time()
event_listeners(turtle_queue, letters)

#Window loops
wn.listen()
wn.mainloop()
