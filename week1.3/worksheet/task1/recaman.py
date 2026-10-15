# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'
sequence = []
seen = set()

if L > 0:
    sequence.append(0)
    seen.add(0)
    
    for k in range(1, L):
        prev = sequence[-1] #previous number is ak-1
        candidate = prev - k # folowing the definition of Recaman's sequence, we first try ak = ak-1 - k
        
        # Logical expression checking criteria matching Wikipedia's definition
        if candidate > 0 and candidate not in seen:
            sequence.append(candidate)
            seen.add(candidate)
        else:
            candidate = prev + k
            sequence.append(candidate)
            seen.add(candidate)


# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence
