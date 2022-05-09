#!/bin/python3
'''
Ben Campbell
3rd Period
Combo menu - let the user build their own sub
'''
#Global variables
sandwichTypes = {"Chicken" : 5.25, "Beef" : 6.25, "Tofu" : 5.75}
drinkSizes = {"Small" : 1.00, "Medium" : 1.75, "Large" : 2.25}
frySizes = {"Small" : 1.00, "Medium" : 1.50, "Large" : 2.00}
userOrder = ["","","",0,0] #Store user order in list: Sandwich, Drink, Fries, Ketchups, Cost
sandwich = 0
drink = 1
fries = 2
ketchups = 3
cost = 4
indexs = {0 : "%s sandwich", 1 : "%s drink", 2 : "%s fries", 3 : "%d ketchup packets", 4 : "Total cost: $%1.2f"}
running = True

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
  

#Get the user's ketchup selection
def getUserKetchups():
  userIn = input("\nHow many ketchup packets would you like?")
  #Error handling
  if userIn.isnumeric():
    #Make sure input is positive or zero then print and return selected amount
    if int(userIn) >= 0:
      print("You selected " + userIn + " packets of ketchup")
      return int(userIn)
    #Recursive error handling
    else:
      print("Enter a positive number")
      return getUserKetchups()
  #Recursive error handling
  else:
    print("Please enter a number 0-9")
    return getUserKetchups()
  
#Sandwich selection process
welcomeUser()

#Loop program to allow user to build multiple meals
while(running):
  #Get user sandwich
  userOrder[sandwich] = getUserSandwich()  
  #Add cost of sandwich to total
  userOrder[cost] += sandwichTypes[userOrder[sandwich]]
  #Get user drink
  userOrder[drink] = getUserDrink()
  #If they chose a drink add cost to total
  if userOrder[drink] in drinkSizes: userOrder[cost] += drinkSizes[userOrder[drink]]
  #Get user fries
  userOrder[fries] = getUserFries()
  #If they chose fries add cost to total
  if userOrder[fries] in frySizes: userOrder[cost] += frySizes[userOrder[fries]]
  #Get user ketchups
  userOrder[ketchups] = getUserKetchups()
  #Add cost of ketchups to total
  userOrder[cost] += .25*userOrder[ketchups]
  #If the user chose a sandwich, drink, and fries give a $1.00 discount
  if userOrder[fries] in frySizes and userOrder[drink] in drinkSizes:
    userOrder[cost] -= 1
    print("\n$1.00 Discount!\n")
  
  #Print the user's final selection by looping through list
  print("Your order was: ")
  for x,item in enumerate(userOrder):
    #Print the item format stored in the indexs dict with the appropriate item inserted
    print(indexs[x] % (item))
  
  #Ask the user if they would like to make another order
  userIn = input("\nWould you like to make another order? (y/n)").strip().lower()
  #Unless they answer yes close program
  if userIn != "y":
    print("Have a good day.")
    running = False
  #Reset program for another order
  else:
    userOrder = ["","","",0,0]