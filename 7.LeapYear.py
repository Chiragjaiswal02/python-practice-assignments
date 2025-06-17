# Write a program to check whether a given year is a leap year.

def isLeapYear(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

year = int(input("Enter the Year: "))

if isLeapYear(year):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is NOT a Leap Year.")
