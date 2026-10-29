# Week 1.5, Session 2: Task 3

# Write a program here that creates two Money objects, prints them,
# then adds them together and prints their sum
from money import Money

money1 = Money(5, 75)
money2 = Money(3, 50)

print(money1)
print(money2)
total_money = money1 + money2
print(total_money)