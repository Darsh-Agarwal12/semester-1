# Week 1.2, Session 2: Task 6

temp=int(input("The machine's temperature in degrees Celsius"))
pressure=int(input("The machine's pressure in PSI"))
status=int(input("The machine's operational status (1 for operating, 0 for stopped)"))

# Temperature Evaluation
is_temp_high = False
if temp > 80:
    print("ALERT: Temperature is too high! Recommend shutting down the machine.")
    is_temp_high = True
elif 50 <= temp<= 80:
    print("Status: Temperature is within safe limits.")
else:
    print("Status: Machine temperature is low, no action needed.")

is_pressure_high = False
if pressure > 100:
    print("ALERT: High pressure detected! Recommend maintenance.")
    is_pressure_high = True
elif 70 <= pressure <= 100:
    print("Status: Pressure is stable.")
else:
    print("Status: Pressure is low, system is operating normally.")

#Status Evaluation
if status == 1:
    if is_temp_high or is_pressure_high:
        print("CRITICAL ALERT: Machine is running in unsafe conditions! Shut it down immediately.")
    else:
        print("Status: Machine is operating normally.")
else:
    print("Status: Machine is stopped.")