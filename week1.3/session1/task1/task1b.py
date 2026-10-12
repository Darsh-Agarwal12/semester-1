# Week 1.3, Session 1: Task 1b

fruit = ['apple','pear','banana','orange']

# loop through the list
while fruit:
	print(fruit.pop())


# Why does this work?
'''This works because python considers non empty collections as True 
while considering empty collections as false, due to which the loop stops after 4th iteration, when the list becomes empty'''

# What features of Python does it rely on?
'''It relies on 3 features of Python:
1. Truth eval: python considers non-empty collections as True and empty ones as False, due to which the loop runs.
2. In-place list manipulation: .pop() func. repeatly removes the last item in the list in the same variables, without creating any copies
3. Dynamic Condition Reval: python re-evaluates the loop condition each time before running it
 '''