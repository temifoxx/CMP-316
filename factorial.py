def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)

# Get user input
number = int(input("Enter a number to find its factorial: "))
result = factorial(number)
print(f"The factorial of {number} is {result}")