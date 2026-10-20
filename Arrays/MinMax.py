n = int(input())                      # Reads the number of elements.
arr = list(map(int, input().split())) # Reads n integers and stores them in a list.

a = []                                # Creates an empty list to store min and max.

min_val = float('inf')                # Initializes minimum with positive infinity. min_val = ∞     max_val = -∞
max_val = float('-inf')                # Initializes maximum with negative infinity.

for i in range(n):                    # Traverses the list n times.
    if arr[i] < min_val:              # Checks whether the current element is smaller than min.
        min_val = arr[i]               # Updates min if a smaller element is found.

    if arr[i] > max_val:              # Checks whether the current element is greater than max.
        max_val = arr[i]               # Updates max if a greater element is found.

a.append(min_val)                      # Adds the minimum value to the list.   a += [min_val, max_val]      # Adds both values to the existing list.
a.append(max_val)                      # Adds the maximum value to the list.

print(a)                               # Prints the minimum and maximum as a list.
