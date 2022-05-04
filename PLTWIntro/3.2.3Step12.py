#Function that uses while loop to print numbers in a range with a certain increment
def whileLoop(start, end, increment):
    #Count variabele
    x = start
    #Positive increments 
    if(increment > 0):
        #Loop while x is less than or equal to the end value
        while(x <= end):
            #Print x then increment it the appropriate amount
            print(x)
            x += increment
    #Negative increments same as above but while conditional is greater than or equal to end
    else:
        while(x >= end):
            print(x)
            x += increment

#Print numbers one to five 
print("One to five:")
whileLoop(1, 5, 1)

#Print numbers ten to one
print("Ten to one:")
whileLoop(10, 1, -1)

#Print even numbers from two to ten
print("Even two to ten:")
whileLoop(2, 10, 2)

#Print odd numbers from nine to one
print("Odd nine to one:")
x = 9
#Loop while x is greater than or equal to one
while(x >= 1):
    #When x divided by 2 and has a remainder of one (odd) print x
    if(x%2 == 1):
        print(x)
    #Increment x
    x -= 1
