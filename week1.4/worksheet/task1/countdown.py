
def countdown(number): 
    '''  
    This recursive function takes a positive integer number  
    and counts the number down to zero printing each value. 
    ''' 
    if number >= 0:
        print(number)
        countdown(number-1)   

num=int(input("Enter a positive integer: "))
if num < 0:
    print("Please enter a positive integer.")
else:
    countdown(num) 