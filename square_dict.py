def create_square_dict(n):
    return {i: i ** 2 for i in range(1, n + 1)}

# Example usage
n = int(input("Enter a number: "))
square_dict = create_square_dict(n)
print(f"Dictionary: {square_dict}")