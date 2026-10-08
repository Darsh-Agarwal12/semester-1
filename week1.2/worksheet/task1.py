# Worksheet 1.2: Task 1 Solution

import sys

try:
    grd=int(input("Enter the grade (range from 0 to 100): "))
    if grd < 0 or grd > 100:
        sys.exit("Error: Grade must be an integer between 0 and 100")
    # Convert the grade to result
    if grd >= 70:
        print(f"{grd} is a Distinction")
    elif grd >= 40:
        print(f"{grd} is a Pass")
    else:
        print(f"{grd} is a Fail")
except ValueError:
    sys.exit("Error: Grade must be an integer between 0 and 100")