# Worksheet 1.2: Task 1 Solution

import sys

try:
    grd=int(input("Enter the grade (range from 0 to 100): "))
    if grd < 0 or grd > 100:
        sys.exit("Error: Grade must be between 0 and 100.")
    # Convert the grade to result
    elif 100 <= grd >= 70:
        print(f"{grd} is a Distinction")
    elif 69 <= grd >= 40:
        print(f"{grd} is a Pass")
    elif 39 <= grd >= 0:
        print(f"{grd} is a Fail")
except ValueError:
    sys.exit("Grade must be an integer between 0 and 100")