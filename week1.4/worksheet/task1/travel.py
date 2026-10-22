
def calculate_travel_distance(tank_capacity, km_per_litre): 
    '''  
    This function calculates the distance a vehicle can travel based on tank  
    capacity (ie how many litres of fuel in tank) and the number of  
    kilometres a vehicle can travel per litre, and returns the  
    distance, rounded to two decimal points. 
    ''' 

    f_capacity = float(tank_capacity) 
    f_kml = float(km_per_litre) 
    distance = round(f_capacity * f_kml, 2) 
    return distance 

details= input("Enter tank capacity and km per litre separated by a space: ").split()
if len(details) != 2:
    print("Please enter exactly two values separated by a space.")
else:  
    tank_capacity, km_per_litre = details
    try:
        distance = calculate_travel_distance(tank_capacity, km_per_litre)
        print(f"The vehicle can travel {distance} kilometres.")
    except ValueError:
        print("Please enter valid numeric values for tank capacity and km per litre.")