# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")
print(f"Modified String 1: {user_string.lower()}") # prints the original string
print(f"Modified String 2: {user_string.upper()}") # prints the original string in uppercase
print(f"Modified String 3: {user_string.strip()}") # prints the original string after removing any leedign and tailing whitespace
print(f"Modified String 4: {user_string.replace('a', '@')}") # print the string by replacing all the occurrences of 'a'with '@'
print(f"Modified String 5: {user_string.capitalize()}") # prints the string with the first character capitalized and rest lowercase
print(f"Modified String 6: {user_string[::-1]}") # prints the string in reversed order
print(f"Modified String 7: {user_string.title()}") # prints the string with first character of each word capitalized
print(f"Modified String 8: {len(user_string)}") # prints the number of characters in the string
print(f"Modified String 9: {user_string.find('a')}") # prints the index of first occurence of 'a' in the string
print(f"Modified String 10: {user_string.count('a')}") # prints the numbwer of times 'a' occurs in the string
print(f"Modified String 11: {user_string.startswith('Hello')}") # prints true if the string starts with 'Hello', otherwise prints false
print(f"Modified String 12: {user_string.endswith('!')}") # prints true if the string ends with '!', otherwise prints false
print(f"Modified String 13: {user_string.isalnum()}") # prints true if the sting is alphanumeric, otherwise prints false
print(f"Modified String 14: {user_string.isalpha()}") # prints true if the sting contains only alphabetic characteres, oterwise prints false
print(f"Modified String 15: {user_string.isdigit()}") # prints true if the string contains only digits, otherwise prints false



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!