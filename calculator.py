def calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Not possible"
        else:
            return num1 / num2
    else: 
        return "Invalid operation"
    
    
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operation (+, -, *, /): ")

result = calculator(num1, num2, operator)
print(f"The result is {result}")