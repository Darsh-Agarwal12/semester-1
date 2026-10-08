# Worksheet 1.2: Task 2 Solution
# Please note that this solution is based on the provided utility function read_numbers().
import sys
from util import read_numbers

num = read_numbers()
if not num:
    sys.exit("Error: no numbers provided.")
max=max(num)
min=min(num)
med=0
if len(num)%2==0:
    med=(sorted(num)[len(num)//2-1]+sorted(num)[len(num)//2])/2
else:
    med=sorted(num)[len(num)//2]

mean=sum(num)/len(num)

print(f"Minimum = {min}")
print(f"Maximum = {max}")
print(f"Mean = {mean}")
print(f"Median = {med}")
