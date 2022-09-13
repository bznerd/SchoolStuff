"""
Ben Campbell 9/13/22
1.1.4 Step 19
Modify their code to make two peaks and a vertical reflection and infinite loop
"""
import turtle as trtl

#Initialize turtle and move to start point
painter = trtl.Turtle()
painter.penup()
painter.goto(-200, 0)
painter.pendown()
painter.speed(0)

#Set variables for position and movement increments
x = -200
y = 0
move_x = 1
move_y = 1

while True:
  #Draw while x position is less than 100 (-100 to 100)
  while (x < 100):
    #Move up until y 100
    while (y < 100):
      x = x + move_x
      y = y + move_y
      painter.goto(x,y)
    #Switch vertical direction
    move_y = -1
    
    #Move down until y 0
    while (y > 0):
      x = x + move_x
      y = y + move_y
      painter.goto(x,y)
    #Switch vertical direction
    move_y = 1
 
  #Switch directions to go back upside down
  y = 0
  move_x = -1
  move_y = -1

  #Draw while x position is greater than -100 (100 to -100)
  while (x > -100):
    #Move down until y -100
    while (y > -100):
      x = x + move_x
      y = y + move_y
      painter.goto(x,y)
    #Switch vertical direction
    move_y = 1

    #Move up until y 0
    while (y < 0):
      x = x + move_x
      y = y + move_y
      painter.goto(x,y)
    #Switch vertical direction
    move_y = -1

  #Switch directions back to start configuration
  move_x = 1
  move_y = 1
 



wn = trtl.Screen()
wn.mainloop()
