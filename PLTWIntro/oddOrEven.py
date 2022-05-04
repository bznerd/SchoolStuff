import random

#Function returns a list of random numbers of the given size with values from 0 to the maxVal
def generateRandomList(size, maxVal):
    #List comprehension black magic fuckery that makes a list of random values
    return [random.randrange(0, maxVal+1) for x in range(size)]

#Return a tuple with a list of odd values and even values from given values
def getOddEvenLists(values):
    #List comprehension loops through values checking for odd/even
    return [x for x in values if x%2 == 1], [x for x in values if x%2 == 0]

#Create a 25 element list with numbers from 0-30
myList = generateRandomList(25, 30)

#Print original list
print("Values are:", *myList)

#Create two lists one with odd values, the other even from myList
odd, even = getOddEvenLists(myList)

#Print out the odd and even lists
print("Odd values are:", *odd)
print("Even values are:", *even)
