"""
Ben Campbell 9/12/22
1.1.4 Step 4
Zero iteration loop and infinite loop
"""
import turtle as turt

#Initiatlize turtle
painter = turt.Turtle()
painter.speed(0)

#Zero iteration loop that would make a square spiral
while painter.heading() > 100:
    for x in range(10):
        painter.forward(x*5)
        painter.right(90)

#Infinite loop drawing a zigzag pattern down the screen
while painter.isdown() == True:
    #Go to top
    painter.penup()
    painter.goto(-100,100)
    painter.pendown()
    painter.seth(0)

    #Draw 10 rows of zig and zaging
    for x in range(10):
        painter.forward(200)
        if x%2 ==0:
            painter.right(90)
            painter.forward(20)
            painter.right(90)
        else:
            painter.left(90)
            painter.forward(20)
            painter.left(90)
