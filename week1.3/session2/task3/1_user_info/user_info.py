# Week 1.3, Session 2: Write User Information to a File


# Prompt the user for their name, age, and favorite colour.

# Open a file called 'user_info.txt' for reading

# Write each piece of information to the file, each on a new line.

# Hints:
# - Remember to add \n for new lines when writing to files


with open('user_info.txt', 'w') as f:
    num= int(input("How many users do you want to enter information for? "))
    for i in range(num):
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        color = input("Enter your favorite colour: ")
        
        f.write(f"{name}\n{age}\n{color}\n")


# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'
