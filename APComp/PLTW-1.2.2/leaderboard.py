"""
Ben Campbell 9/23/22
The leaderboard module to be used in Activity 1.2.2
"""

# set the levels of scoring
bronze_score = 15
silver_score = 20
gold_score = 25

# return names in the leaderboard file
def get_names(file_name):
  leaderboard_file = open(file_name, "r")  # be sure you have created this

  # use a for loop to iterate through the content of the file, one line at a time
  # note that each line in the file has the format "leader_name,leader_score" for example "Pat,50"
  names = []
  for line in leaderboard_file:
    leader_name = ""
    index = 0

    # Loop to find , and record leader name
    while (line[index] != ","):
      leader_name = leader_name + line[index] 
      index = index + 1

    # Add name to names list
    names.append(leader_name)

  leaderboard_file.close()

  #  Return name list
  return names 

  
# return scores from the leaderboard file
def get_scores(file_name):
  leaderboard_file = open(file_name, "r")  # be sure you have created this

  scores = []
  # Loop over lines
  for line in leaderboard_file:
    leader_score = ""    
    index = 0

    # Loop until , and move one past it
    while (line[index] != ','):
        index += 1
    index += 1

    # Loop till end of line and record score
    while (line[index] != '\n'):
        leader_score += line[index]
        index += 1

    # Add score to score list
    scores.append(int(leader_score))
   
  leaderboard_file.close()

  # Return scrore list
  return scores 


# update leaderboard by inserting the current player and score to the list at the correct position
def update_leaderboard(file_name, leader_names, leader_scores,  player_name, player_score):

  index = 0
  # Loop over scores
  for x in range(len(leader_scores)):
    # Check if this is positon for player score
    if (player_score >= leader_scores[x]):
      break
    else:
      index = index + 1
  
  # Insert new score and player
  leader_names.insert(index, player_name)
  leader_scores.insert(index, player_score)

  # Reduce list to 5 elements
  leader_names = leader_names[:5]
  leader_scores =  leader_scores[:5]
  
  # Add latest scores to file
  
  leaderboard_file = open(file_name, "w")  # this mode opens the file and erases its contents for a fresh start
 
  # Loop over scores and write them to file
  for index in range(len(leader_names)):
    leaderboard_file.write(leader_names[index] + "," + str(leader_scores[index]) + "\n")

  leaderboard_file.close()
  

# draw leaderboard and display a message to player
def draw_leaderboard(high_scorer, leader_names, leader_scores, turtle_object, player_score):
  
  # clear the screen and move turtle object to (-200, 100) to start drawing the leaderboard
  font_setup = ("Arial", 20, "normal")
  turtle_object.clear()
  turtle_object.penup()
  turtle_object.goto(-160,100)
  turtle_object.hideturtle()
  turtle_object.down()

  # loop through the lists and use the same index to display the corresponding name and score, separated by a tab space '\t'
  for index in range(len(leader_names)):
    turtle_object.write(str(index + 1) + "\t" + leader_names[index] + "\t" + str(leader_scores[index]), font=font_setup)
    turtle_object.penup()
    turtle_object.goto(-160,int(turtle_object.ycor())-50)
    turtle_object.down()
  
  # move turtle to a new line
  turtle_object.penup()
  turtle_object.goto(-160,int(turtle_object.ycor())-50)
  turtle_object.pendown()

  # If it's a high scorer display congrats, else don't
  if high_scorer:
    turtle_object.write("Congratulations!\nYou made the leaderboard!", font=font_setup)
  else:
    turtle_object.write("Sorry!\nYou didn't make the leaderboard.\nMaybe next time!", font=font_setup)

  # move turtle to a new line
  turtle_object.penup()
  turtle_object.goto(-160,int(turtle_object.ycor())-50)
  turtle_object.pendown()
  
  # Display a gold/silver/bronze message if player earned a gold/silver/or bronze medal; display nothing if no medal 
  if not high_scorer: return
  if leader_scores.index(player_score) == 0: turtle_object.write("You earned a gold medal!", font=font_setup)
  if leader_scores.index(player_score) == 1: turtle_object.write("You earned a silver medal!", font=font_setup)
  if leader_scores.index(player_score) == 2: turtle_object.write("You earned a bronze medal!", font=font_setup)
