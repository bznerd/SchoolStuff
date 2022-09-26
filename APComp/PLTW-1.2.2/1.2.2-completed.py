"""
Ben Campbell 9/22/22
1.2.1 Step 50

"""

#-----import statements-----
import turtle
import random
import leaderboard as lb

#-----game configuration----
#Spot parameters
shape_fill = "pink"
shape_size = 2
shape = "circle"

#Score/timer variable, timer interval, and global time up flag
score = {"score": 0, "time": 15}
timer_interval = 1000
timer_up = False

#Default font variable
font_setup = ("Arial", 20, "normal")

leaderboard_file = "a122_leaderboard.txt"
player_name = input("What is your name? ")

#-----initialize turtle-----
#Intialize spot turtle to move around screen (pink circle)
spot = turtle.Turtle(shape=shape)
spot.fillcolor(shape_fill)
spot.shapesize(shape_size)
spot.penup()
spot.speed(0)

#Intialize score_writer turtle to display score at the top of the screen
score_writer = turtle.Turtle()
score_writer.speed(0)
score_writer.penup()
score_writer.goto(-100,170)
score_writer.hideturtle()

#-----game functions--------
# Event for mouse clock on spot
def spot_clicked(x, y):
    #If game finished hide turtle
    if timer_up:
        spot.hideturtle()
    # Else update the score and move to new position
    else:
        update_score()
        change_pos() 

#Move spot to random position on screen
def change_pos():
    new_x = random.randint(-200,200)
    new_y = random.randint(-150, 130)
    spot.goto(new_x, new_y)

#Add one to the score and display with score_writer
def update_score():
    global score
    score["score"] += 1
    score_writer.clear()
    score_writer.write(f"Score: {score['score']}   Time: {score['time']}", font=font_setup)

# Timer function on a 1 second interval
def timer():
    global score
    global timer_up
    #If time is not up write time, decrement time, and call timer function again with 1 second timer
    if score["time"] > 0:
        score_writer.clear()
        score_writer.write(f"Score: {score['score']}   Time: {score['time']}", font=font_setup)
        score["time"] -= 1
        score_writer.getscreen().ontimer(timer, timer_interval)

    #If time is up, set global timer_up variable and write time up
    else:
        timer_up = True
        score_writer.clear()
        score_writer.write(f"Time's up! Score: {score['score']}", font=font_setup)
        manage_leaderboard()
        

# manages the leaderboard for top 5 scorers
def manage_leaderboard():

  global score
  global spot 

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file)
  leader_scores_list = lb.get_scores(leaderboard_file)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score["score"] >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file, leader_names_list, leader_scores_list, player_name, score["score"])
    leader_names_list = lb.get_names(leaderboard_file)
    leader_scores_list = lb.get_scores(leaderboard_file)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score["score"])

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score["score"])


#-----events----------------
#Intialize screen
wn = turtle.Screen()
wn.setup(width=620,height=550)

#Turtle click and timer events
spot.onclick(spot_clicked)
wn.ontimer(timer, timer_interval)

#Main window loop
wn.mainloop()
