# Week 1.5, Session 2: Task 5

# Write a program here to create a Dataset containing data
# from a file named by the user

# Your program should display dataset size, mean and median,
# followed by the individual values (using a for loop)
from data import Dataset

filename = input("Enter the filename containing the dataset: ")
dataset = Dataset(filename)
index= int(input("Enter the index of the value you want to access: "))
print(f"Dataset size: {len(dataset)}")
print(f"Dataset mean: {dataset.mean()}")
print(f"Dataset median: {dataset.median()}")
print(f"Value at index {index}: {dataset[index]}")
