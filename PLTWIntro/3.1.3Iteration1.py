'''
Ben Campbell
3rd Period
Combo menu - let the user build their own sub
'''
#Global variables
sandwichTypes = {"Chicken" : 5.25, "Beef" : 6.25, "Tofu" : 5.75}
userSandwich = ""
userCost = 0

#Functions for program execution

#Print welcome message
def welcomeUser():
  print("Welcome to the Sandwich Shop")

#Query user for sandwich type
def getUserSandwich():
  print("Please select one of the following sandwich types: ")
  out = ""
  #Add sandwich types from sandwhichTypes dict and prices into one string
  for x, sandwich in enumerate(sandwichTypes):
    out += sandwich + ": $" + str(sandwichTypes[sandwich])
    if x < len(sandwichTypes) - 1: out += ", "
  #Print sandwhich types and query user input
  userIn =  input(out)
  #clean up userIn
  userIn = userIn.lower().strip().replace(" ", "").capitalize()
  #Invalid input handling. Prints error message and recursively runs this funtion again
  #If input is valid prints out selection and cost to user and returns the selection
  if userIn in sandwichTypes:
    print("You chose " +  userIn + " for $" + str(sandwichTypes[userIn]))
    return userIn
  #recursive error handling
  else:
    print("Not an option please choose again")
    return getUserSandwich()

  
  
#Sandwich selection process

#Send welcome message
welcomeUser()
#Get user sandwich
userSandwich = getUserSandwich()
#Add cost of sandwich to total
userCost += sandwichTypes[userSandwich]