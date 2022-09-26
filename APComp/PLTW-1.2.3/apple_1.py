#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
text = ('Arial', 15, 'normal')
tree_bounds = ((-100,-100),(100,100))

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("background.gif")
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()
apple.penup()

typer = trtl.Turtle()
typer.penup()
typer.hideturtle()
typer.color("white")

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def add(*coords):
    total = [0 for x in range(len(coords[0]))]
    for pair in coords:
       total = [total[x] + pair[x] for x in range(len(total))] 
    return tuple(total)

def move_to_ground(turtle, ground_y, speed=3):
    turtle.seth(270)
    orig_speed = turtle.speed()
    turtle.speed(speed)
    turtle.goto(add(turtle.pos(), (turtle.xcor(), ground_y)))
    turtle.speed(orig_speed)

def draw_letter(turtle, letter):
    turtle.goto(add(turtle.pos(), (0,-30)))
    turtle.write(letter, align="center", font=text)

def fall_sequence():
    move_to_ground(apple, -180)
    apple.hideturtle()
    typer.clear()

def reset_apple(turtle, letters):
    location = (rand.randint(tree_bounds[0][0], treebounds[1][0]), rand.randint(tree_bounds[0][1], treebounds[1][1])
    letter = ''
    if letters != []:
        letter = letters.pop(rand.randint(len(letters))

    turtle.goto(location)
    return letter

def place_apple(turtle, image=apple_image):
    turtle.shape(image)
    wn.tracer(False)
    draw_letter(typer, reset_apple(turtle, letter_list))
    wn.update()
    wn.tracer(True)



#-----function calls-----
for x in range(apple_count):
    turtles.append(

draw_apple(apple)
draw_letter(typer, "A", apple.pos())

wn.onkeypress(fall_sequence, "a")

wn.listen()
wn.mainloop()
