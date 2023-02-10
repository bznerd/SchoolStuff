def factorial(n):
    return (n if n <= 1 else n * factorial(n-1))

def main():
        user_in = int(input("Enter an integer to calculate the factorial: "))
        if user_in < 0:
            print("Must be greater than zero")
            return main()
        
        print(f"The factorial of {user_in} equals: {factorial(user_in)}")

main()
