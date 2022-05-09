'''
Ben Campbell
3rd Period
Combo menu - let the user build their own sub
'''
#Global variables
sandwichTypes = {"Chicken" : 5.25, "Beef" : 6.25, "Tofu" : 5.75}
drinkSizes = {"Small" : 1.0, "Medium" : 1.75, "Large" : 2.25}
userSandwich = ""
userDrink = ""
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


#Query user for drink
def getUserDrink():
  userIn = input("Would you like a drink? (y/n)").strip().lower()
  #Ask user if they want a drink or not
  if userIn == "y":
    out = ""
    print("Please choose a drink size: ")
    #Add drink sizes from drinkSizes dict and prices into one string
    for x, drink in enumerate(drinkSizes):
      out += drink + ": $" + str(drinkSizes[drink])
      if x < len(drinkSizes) - 1: out += ", "
    #Print drink types and query user input
    userIn =  input(out)
    #Clean up userIn
    userIn = userIn.lower().strip().replace(" ", "").capitalize()
    #Error handling, print user selection, and return their selection (same as sandwich function)
    if userIn in drinkSizes:
      print("You chose " +  userIn + " for $" + str(drinkSizes[userIn]))
      return userIn
    else:
      print("Not an option please choose again")
      return getUserDrink()
  #If the user does not want a drink print that message and return no
  elif userIn == "n":
    print("You chose no drink")
    return "None"
  #Error handling for yes/no, runs function recursively
  else:
    print("Invalid input")
    return getUserDrink()
  
  
#Sandwich selection process

#Send welcome message
welcomeUser()
#Get user sandwich
userSandwich = getUserSandwich()
#Add sandwich cost to total
userCost += sandwichTypes[userSandwich]
#Get user drink size
userDrink = getUserDrink()
#If they chose a drink add the cost to the total
if userDrink in drinkSizes: userCost += drinkSizes[userDrink]
#Display current total cost
print("Current total: $" + str(userCost))