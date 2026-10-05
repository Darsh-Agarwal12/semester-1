# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?

both = fruit.intersection(vegetables)
# tomato
print(both)

# Why does the following code diplay five items?
# it prints 5 items because it add the unique items from fruit and vegetables to food
food = fruit.union(vegetables)
print(food)

# Add an item to fruit
fruit.add("banana")
print(fruit)

# Remove an item from vegetables
vegetables.discard("leek")
print(vegetables)
# Find and display symmetric difference of the two sets
diff=fruit.symmetric_difference(vegetables)
print(diff)