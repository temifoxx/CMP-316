def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
        return True
    return False

# Get user input
year = int(input("Enter a year: "))

# Check and print result
if is_leap_year(year):
    print(f"{year} is a Leap Year! 🎉")
else:
    print(f"{year} is NOT a Leap Year! ❌")
