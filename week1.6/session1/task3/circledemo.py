# Week 1.6, Session 1: Task 3

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)
from shapes import Circle
from point import Point

radius= int(input("Enter radius: "))
pos = Point(int(input("Enter x position: ")), int(input("Enter y position: ")))
color = input("Enter colour(default is red): ")
if color=="":
    color="red"
circle = Circle(radius, pos, color)

print(circle)
print(f"Area: {circle.area()}")
print(f"Perimeter: {circle.perimeter()}")