# Lambda function to add 10 to a given number
add_10 = lambda x: x + 10

# Lambda function to multiply argument x with argument y
multiply = lambda x, y: x * y

# Example usage
number = int(input("Enter a number to add 10: "))
print(f"Result after adding 10: {add_10(number)}")

x = int(input("Enter the first number to multiply: "))
y = int(input("Enter the second number to multiply: "))
print(f"Result of multiplication: {multiply(x, y)}")