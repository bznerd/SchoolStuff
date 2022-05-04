import random

#Function returns a list of random numbers of the given size with values from 0 to the maxVal
def generateRandomList(size, maxVal):
    #List comprehension black magic fuckery that makes a list of random values
    return [random.randrange(0, maxVal+1) for x in range(size)]

#Function returns a lsit of values less than the given value from the given list
def getLessThan(values, lessThan):
    #List comprehension to generate a list from the original list only including values less than lessThan
    return [x for x in values if x < lessThan]

#Generate a 20 item list with values 0-10
myList = generateRandomList(20, 10)

#Print list
print("Values are: ", *myList)

#Print list of values less than 5 form myList
print("Vals below 5 are:" , *getLessThan(myList, 5))
