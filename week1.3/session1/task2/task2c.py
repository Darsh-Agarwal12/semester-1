# Week 1.3, Session 1: Task 2c

# open a named text file for reading using open() function
# the `with` statement closes the file automatically as the block of code finishes executing

with open('/workspaces/semester-1/week1.3/session1/task2/file_data.txt', 'r') as file:  

    while True:
        # read by character
        char = file.read(1)            # read exactly 1 character from the file      
        if not char: 
            break

        print(char)

# This example shows a common while-break pattern - reading from a file

# Test it - you can also modify the text file to add more data 

# We will study this in more detail later on, but in this case we read character by character
# We use 'break' to exit the reading process at the end of the file.

# Why do we use an infinite 'while True' loop for this process?
#We use an infinete 'While True' loop for this process because we don't know the length of the file, in order to not miss anything unread in the file.