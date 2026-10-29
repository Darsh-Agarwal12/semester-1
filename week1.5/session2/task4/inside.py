# Week 1.5, Session 2: Task 4
# A program that demonstrates use of the __contains__() method in the Circle class

from geometry import Point, Circle

my_circle = Circle(5.0, Point(0.0, 0.0))
print(f"Testing with Circle: {my_circle}\n" + "-"*40)

p1 = Point(2.0, 3.0)
print(f"Is Point {p1} inside? {p1 in my_circle}")  
p2 = Point(6.0, 1.0)
print(f"Is Point {p2} inside? {p2 in my_circle}") 


p3 = Point(5.0, 0.0)
print(f"Is Point {p3} inside? {p3 in my_circle}")  
