# Week 1.2, Session 2: Task 6

temp=int(input("The machine's temperature in degrees Celsius"))
pressure=int(input("The machine's pressure in PSI"))
status=int(input("The machine's operational status (1 for operating, 0 for stopped)"))

if temp>=80:
    print("Temperature is too high! Shut down the machine")
elif 50<=temp<80:
    print("Temperature is within safe limits")
else:
    print("Temperature is low, no action needed")

if pressure>=100:
    print("Alert high pressure detected! Maintenance recquired.")
elif 70<=pressure<100:
    print("Stable Presseure")
else:
    print("Low Pressure, normal system operation")

