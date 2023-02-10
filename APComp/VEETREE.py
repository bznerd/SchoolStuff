import turtle as turt

stick = turt.Turtle()

def draw_fractal(turtle, branches, length=10):
    draw_fractal_internal(turtle, branches, length)

def draw_fractal_internal(turtle, branches, length):
    if branches == 0: return
    turtle.setheading(-135)
    turtle.pendown()
    turtle.forward(length)
    draw_fractal(turtle, branches - 1, length//2)
    turtle.setheading(-135)
    turtle.backward(length)
    turtle.setheading(-45)
    turtle.pendown()
    turtle.forward(length)
    draw_fractal(turtle, branches - 1, length//2)
    turtle.setheading(-45)
    turtle.backward(length)


def draw_tree_internal(turtle, branches, length, colored_branches=2):
    if branches <= colored_branches: turtle.pencolor('green')
    else: turtle.pencolor('brown')
    if branches == 1:
        stick.forward(length)
        stick.backward(length)

    else:
        stick.forward(length)
        stick.left(15)
        draw_tree(turtle, branches - 1, .75 * length, colored_branches)
        stick.right(30)
        draw_tree(turtle, branches - 1, .75 * length, colored_branches)
        stick.left(15)
        stick.back(length)

    if branches + 1 <= colored_branches: turtle.pencolor('green')
    else: turtle.pencolor('brown')


def draw_snowflake_arm(turtle, recursions, size):
    if recursions == 1:
        turtle.forward(size)
    else:
        draw_snowflake_arm(turtle, recursions - 1, size/3)
        turtle.left(60)
        draw_snowflake_arm(turtle, recursions - 1, size/3)
        turtle.right(120)
        draw_snowflake_arm(turtle, recursions - 1, size/3)
        turtle.left(60)
        draw_snowflake_arm(turtle, recursions - 1, size/3)

def draw_snowflake(turtle, recursions, size, sides):
    turtle.penup()
    turtle.pencolor('blue')
    turtle.pensize(4)
    turtle.goto(-size/2, 0)
    turtle.setheading(0)
    turtle.pendown()

    for x in range(6*sides):
        draw_snowflake_arm(turtle, recursions, size)
        turtle.left(150)

draw_snowflake(stick, 3, 300, 3)
turt.Screen().mainloop()
