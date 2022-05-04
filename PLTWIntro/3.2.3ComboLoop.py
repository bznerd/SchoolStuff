#!/bin/python3
'''
Ben Campbell
3rd Period
Combo menu - let the user build their own sub
Iteration 5 adds multiple order options
'''
#Global variables
sandwichTypes = {"Chicken" : 5.25, "Beef" : 6.25, "Tofu" : 5.75}
drinkSizes = {"Small" : 1.00, "Medium" : 1.75, "Large" : 2.25}
frySizes = {"Small" : 1.00, "Medium" : 1.50, "Large" : 2.00}
#Order variable stores a dict with a list of orders, the number of ketchup packets ordered, and the total cost
order = {"items" : [], "ketchups" : 0, "cost" : 0}

#Functions for program execution

#Print welcome message
def welcomeUser():
  print("Welcome to the Sandwich Shop\n")

#Print a formatted message with the inputed cost
def printTotal(cost):
  print("\nTotal cost is: $%1.2f" % (cost))

#Ask the user to confirm y/n for a given message. returns true/false
def getConfirmation(msg):
    #Get userinput for message
    userIn = input(msg + " (y/n) ").strip().replace(" ",'').lower()
    #Return appropriate value for answer
    if(userIn == 'y'):
        return True
    elif(userIn == 'n'):
        return False
    #Recursive error handling
    else:
        print("Invalid input try again")
        return getConfirmation(msg)

#Return a formmated order string
def formatOrder(order):
  return "%s sandwich, %s drink, %s fry" % (order[0], order[1].replace(" drink",''), order[2].replace(" fries",''))


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
  userIn =  input(out+' ')
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
  userIn = input("\nWould you like a drink? (y/n) ").strip().lower()
  #Ask user if they want a drink or not
  if userIn == "y":
    out = ""
    print("Please choose a drink size: ")
    #Add drink sizes from drinkSizes dict and prices into one string
    for x, drink in enumerate(drinkSizes):
      out += drink + ": $%1.2f" % (drinkSizes[drink])
      if x < len(drinkSizes) - 1: out += ", "
    #Print drink types and query user input
    userIn =  input(out+' ')
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
    return "no drink"
  #Error handling for yes/no, runs function recursively
  else:
    print("Invalid input")
    return getUserDrink()

#Query user for fries
def getUserFries():
  userIn = input("\nWould you like fries? (y/n) ").strip().lower()
  #Ask user if they want fries or not
  if userIn == "y":
    out = ""
    print("Please choose a fry size: ")
    #Add fry sizes from frySizes dict and prices into one string
    for x, fry in enumerate(frySizes):
      out += fry + ": $%1.2f" % (frySizes[fry])
      if x < len(frySizes) - 1: out += ", "
    #Print fry types and query user input
    userIn =  input(out+' ')
    #Clean up userIn
    userIn = userIn.lower().strip().replace(" ", "").capitalize()
    #Error handling
    if userIn in frySizes:
      #If the user choses small ask if they want to mega-size
      if userIn == "Small":
        megaSize = input("Would you like to mega-size your fries? (y/n) ").strip().lower()
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
    return "no fries"
  #Recursive error handling
  else:
    print("Invalid input")
    return getUserFries() 

#Get the user's ketchup selection
def getUserKetchups():
  userIn = input("\nHow many ketchup packets would you like? ")
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
orderProcess = [getUserSandwich, getUserDrink, getUserFries]

#Loop program to allow user to enter multiple orders
while(True):
  #Welcome message
  welcomeUser()

  #Loop meal orders (excludes ketchups) for multiple enteries
  while(True):
    #If there are already orders placed display them to the use        
    if order['items']:
      print("Order so far:")

      #Loop through orders and print them
      for suborder in order['items']:
        print(formatOrder(suborder))
    
    #Else first order message
    else: print("Enter the first meal")

    #For each given order add a list of items to the order list with a list comphrehension that goes through each user in function
    order['items'].append([x() for x in orderProcess])
    
    #Break loop if user is done entering orders
    if not getConfirmation("\nWould you like to order more meals?"): break
  
  #Add number of ketchups to order with getUserKetchups()
  order['ketchups'] += getUserKetchups()

  #Add cost of every item ordered to cost variable
  for suborder in order['items']:
    items = 0
    if suborder[0] in sandwichTypes:
      order['cost'] += sandwichTypes[suborder[0]]
      items += 1
    if suborder[1] in drinkSizes:
      order['cost'] += drinkSizes[suborder[1]]
      items += 1
    if suborder[2] in frySizes:
      order['cost'] += frySizes[suborder[2]]
      items += 1

    #Count items ordered for each order and give combo discount if all three were ordered
    if items == 3:
      print("\nYou get a total combo discount of $1.00!")
      order['cost'] -= 1
      
  #Add ketchup cost to order
  order['cost'] += .25*order['ketchups']
  print("\nYou had the following orders:")

  #Print out each order
  for suborder in order['items']:
    print(formatOrder(suborder))

  #Print number of ketchup packets
  print("\nYou ordered %d ketchup packets" % order['ketchups'])

  #Print total cost
  printTotal(order['cost'])
  
  #Exit program if user is done, if not reset order variable
  if not getConfirmation("\nWould you like to make another order?"): break
  order = {"items" : [], "ketchups" : 0, "cost" : 0}
