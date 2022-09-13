#   a114_nested_loops_2.py
import turtle as trtl

color1 = "orange"
color2 = "purple"

wn = trtl.Screen()
width = 400
height = 300

painter = trtl.Turtle()
painter.speed(0)
painter.color(color1)

answer = "y"
while (answer == "y"):
  wn.clearscreen()  
  painter.goto(0,0)
  space = 1

  angle = int(input("angle:"))
  seg = int(360/angle)

  while painter.ycor() < height:
    painter.pencolor(color1 if (space//100) % 2 == 0 else color2)
    painter.fillcolor(color1 if (space//100) % 2 == 0 else color2)
    painter.right(angle)
    painter.forward(1.5 * space + 5) # experiment
    painter.begin_fill()
    painter.circle(3)
    painter.end_fill()
    space = space + 1

  answer = input("again?")

wn.bye()