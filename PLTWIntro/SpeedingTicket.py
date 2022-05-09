'''
Ben Campbell
3rd Period
Keyboard input and conditionals practice: Speeding ticket generator
'''

#global variables
ticket = 75 #Ticket begins at $75
limit = int(input("What is the posted speed limit? (mph)"))
#Speed limit input
speed = int(input("How fast was the car going? (mph)"))
#Recorded speed input
schoolZone = bool(input("Was the car in a school zone? (y/n)").upper() == "Y")
#Record true/false whether or not it was a school zone

ticket += 6*(speed-limit)
#Add $6 dollars to the ticket for every mph over the speed limit
if speed-limit > 30:
  ticket += 160
#Add $160 if the driver went more than 30 mph over

if schoolZone:
  ticket = 2*ticket
#If it was in a school zone double the ticket
  
print("The ticket amount is: $" + str(ticket))
#Display the total value of the ticket