# Week 1.3, Session 1: Task 2a

k = 2
while True:
    k = 2 * k 
    

# As written this is an infinite loop.
# If you run it, use <Ctrl>C to exit the running program.

# 1. Add a break statement to exit the loop if k>200
    if k>200:
        break
    else:
        print(k)
    

# 2. Rewrite the code to directly use the while loop instead of break.
a=2
while a<200:
    print(a)
    a= a*2