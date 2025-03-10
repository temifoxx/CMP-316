def multiplication_table(number):
    for i in range(1, 12):
        print(f"{number} * {i} = {number * i}")

number = int(input("Enter a number: "))
multiplication_table(number)