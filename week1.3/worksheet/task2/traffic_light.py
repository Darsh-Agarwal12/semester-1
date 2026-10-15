"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Darsh Agarwal
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"

for i in range(maxtime):
    print(f"Time {systime:03} State {state}")
    systime += 1
    states[state] -= 1
    
    if states[state] == 0:
        if state == "red":
            state = "red_amber"
        elif state == "red_amber":
            state = "green"
        elif state == "green":
            state = "amber"
        elif state == "amber":
            state = "red"
        
        # Reset the timer for the new state
        states[state] = {"red":4, "red_amber":3, "green":5, "amber":3}[state]

print(f"Time {systime:03} State {state}")

# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14