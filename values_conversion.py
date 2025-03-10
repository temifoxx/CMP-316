def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def kilograms_to_milligrams(kilograms):
    return kilograms * 1000000

# Example usage
celsius = float(input("Enter temperature in Celsius: "))
print(f"{celsius} Celsius is {celsius_to_fahrenheit(celsius)} Fahrenheit")

kilometers = float(input("Enter distance in kilometers: "))
print(f"{kilometers} kilometers is {kilometers_to_miles(kilometers)} miles")

kilograms = float(input("Enter weight in kilograms: "))
print(f"{kilograms} kilograms is {kilograms_to_milligrams(kilograms)} milligrams")