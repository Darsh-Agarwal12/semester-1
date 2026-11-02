from feed import QuakeFeed
from dataset import QuakeDataset

level = input("Enter significance level (e.g., all, 1.0, 4.5, significant): ").strip()
period = input("Enter time period (e.g., hour, day, week, month): ").strip()

feed = QuakeFeed(level, period)
dataset = QuakeDataset(feed)

dataset.read_feed()


print(dataset)
print(f"Mean depth = {round(dataset.mean_depth(), 2)} km")
print(f"Mean magnitude = {round(dataset.mean_magnitude(), 1)}")
print() 
strongest = dataset.strongest_quake()

time_str = strongest.when.strftime('%H:%M:%S')
date_str = strongest.when.strftime('%Y-%m-%d')

print(f"Strongest quake occurred at {time_str} on {date_str}")
print(f"at {round(strongest.longitude, 1)}° longitude, {round(strongest.latitude, 1)}° latitude")
print(f"The depth was {round(strongest.depth, 1)} km")
print(f"The magnitude was {round(strongest.magnitude, 1)}")
print(f"The weakest quake occurred at {time_str} on {date_str}")

weakest = dataset.weakest_quake()
deepest = dataset.deepest_quake()

time_str = weakest.when.strftime('%H:%M:%S')
date_str = weakest.when.strftime('%Y-%m-%d')

print(f"The weakest quake occurred at {time_str} on {date_str}")
print(f"at {round(weakest.longitude, 1)}° longitude, {round(weakest.latitude, 1)}° latitude")
print(f"The depth was {round(weakest.depth, 1)} km")
print(f"The magnitude was {round(weakest.magnitude, 1)}")

print(f"The deepest quake occurred at {time_str} on {date_str}")
print(f"at {round(deepest.longitude, 1)}° longitude, {round(deepest.latitude, 1)}° latitude")
print(f"The depth was {round(deepest.depth, 1)} km")
print(f"The magnitude was {round(deepest.magnitude, 1)}")

export = input("Do you want to export the data to a CSV file? (y/n): ").strip().lower()
if export == 'y':
    filename = input("Enter the filename (e.g., quakes.csv): ").strip()
    dataset.export_to_csv(filename)
    print(f"Data exported to {filename}")
    