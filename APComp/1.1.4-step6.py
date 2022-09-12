"""
Ben Campbell 9/12/22
1.1.4 step 6
Infinite loop ask user for two numbers
Exit when they are evenly divisible
"""

#Recursive function to test even
def user_even():
    #Get two numbers 
    a = int(input("Enter first number: "))
    b = int(input("Enter second nummber: "))

    #If not divisible call function again
    if a%b != 0:
        print(f"{a} is not divisible by {b}")
        user_even()
    else: print(f"{a} is divisible by {b}, {a//b} times")

#Program entrypoint
user_even()
