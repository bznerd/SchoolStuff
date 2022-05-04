#Function that iterates through a range and prints each value
def rangeLoopPrint(start, end, increment):
    #Modify end point to make it inclusive of the end value
    end += increment
    #Loop through range and print
    for x in range(start, end, increment):
        print(x)

#Print numbers one to nine
print("One to nineteen:")
rangeLoopPrint(1, 19, 1)

#Print numbers twenty to one
print("Twenty to one:")
rangeLoopPrint(20, 1, -1)

#Print even numbers from two to ten
print("Even two to ten:")
rangeLoopPrint(2, 10, 2)

#Print odd numbers from nine to one
print("Odd nine to one:")
rangeLoopPrint(9, 1, -2)
