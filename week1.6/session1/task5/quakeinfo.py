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
