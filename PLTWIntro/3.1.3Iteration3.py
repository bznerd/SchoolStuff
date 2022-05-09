'''
Ben Campbell
3rd Period
Combo menu - let the user build their own sub
'''
#Global variables
sandwichTypes = {"Chicken" : 5.25, "Beef" : 6.25, "Tofu" : 5.75}
drinkSizes = {"Small" : 1.00, "Medium" : 1.75, "Large" : 2.25}
frySizes = {"Small" : 1.00, "Medium" : 1.50, "Large" : 2.00}
userSandwich = ""
userDrink = ""
userFries = ""
userCost = 0

#Functions for program execution

#Print welcome message
def welcomeUser():
  print("Welcome to the Sandwich Shop")

#Print a formatted message with the inputed cost
def printTotal(cost):
  print("\nTotal cost is: $%1.2f" % (cost))

#Query user for sandwich type
def getUserSandwich():
  print("\nPlease select one of the following sandwich types: ")
  out = ""
  #Add sandwich types from sandwhichTypes dict and prices into one string
  for x, sandwich in enumerate(sandwichTypes):
    out += sandwich + ": $%1.2f" % (sandwichTypes[sandwich])
    out.format(price = sandwichTypes[sandwich])
    if x < len(sandwichTypes) - 1: out += ", "
  #Print sandwhich types and query user input
  userIn =  input(out)
  #clean up userIn
  userIn = userIn.lower().strip().replace(" ", "").capitalize()
  #Invalid input handling. Prints error message and recursively runs this funtion again
  #If input is valid prints out selection and cost to user and returns the selection
  if userIn in sandwichTypes:
    print("You chose " +  userIn + " for $%1.2f" % (sandwichTypes[userIn]))
    return userIn
  #recursive error handling
  else:
    print("Not an option please choose again")
    return getUserSandwich()

#Query user for drink
def getUserDrink():
  userIn = input("\nWould you like a drink? (y/n)").strip().lower()
  #Ask user if they want a drink or not
  if userIn == "y":
    out = ""
    print("Please choose a drink size: ")
    #Add drink sizes from drinkSizes dict and prices into one string
    for x, drink in enumerate(drinkSizes):
      out += drink + ": $%1.2f" % (drinkSizes[drink])
      if x < len(drinkSizes) - 1: out += ", "
    #Print drink types and query user input
    userIn =  input(out)
    #Clean up userIn
    userIn = userIn.lower().strip().replace(" ", "").capitalize()
    #Error handling, print user selection, and return their selection (same as sandwich function)
    if userIn in drinkSizes:
      print("You chose " +  userIn + " for $%1.2f" % (drinkSizes[userIn]))
      return userIn
    else:
      print("Not an option please choose again")
      return getUserDrink()
  #If the user does not want a drink print that message and return no
  elif userIn == "n":
    print("You chose no drink")
    return "no"
  #Error handling for yes/no, runs function recursively
  else:
    print("Invalid input")
    return getUserDrink()

#Query user for fries
def getUserFries():
  userIn = input("\nWould you like fries? (y/n)").strip().lower()
  #Ask user if they want fries or not
  if userIn == "y":
    out = ""
    print("Please choose a fry size: ")
    #Add fry sizes from frySizes dict and prices into one string
    for x, fry in enumerate(frySizes):
      out += fry + ": $%1.2f" % (frySizes[fry])
      if x < len(frySizes) - 1: out += ", "
    #Print fry types and query user input
    userIn =  input(out)
    #Clean up userIn
    userIn = userIn.lower().strip().replace(" ", "").capitalize()
    #Error handling
    if userIn in frySizes:
      #If the user choses small ask if they want to mega-size
      if userIn == "Small":
        megaSize = input("Would you like to mega-size your fries? (y/n)").strip().lower()
        if megaSize == "y": userIn = "Large"
        #error handling
        elif megaSize != "n":
          print("Invalid input")
          return getUserFries()
      #Print their selection (updated for mega-size) then return selection
      print("You chose " +  userIn + " for $%1.2f" % (frySizes[userIn]))
      return userIn
    #recursive error handling
    else:
      print("Not an option please choose again")
      return getUserFries()
  #Print no fries and return no if the user doesn't want fries 
  elif userIn == "n":
    print("You chose no fries")
    return "no"
  #Recursive error handling
  else:
    print("Invalid input")
    return getUserFries()
  
#Sandwich selection process

#Send welcome message
welcomeUser()
#Get user sandwich
userSandwich = getUserSandwich()
#Add cost of sandwich to total
userCost += sandwichTypes[userSandwich]
#Get user drink size
userDrink = getUserDrink()
#If the user chose a drink add it's cost to the total
if userDrink in drinkSizes: userCost += drinkSizes[userDrink]
#Get user fry choice
userFries = getUserFries()
#If the user chose fries add the cost to the total
if userFries in frySizes: userCost += frySizes[userFries]
#Print current total cost
printTotal(userCost)