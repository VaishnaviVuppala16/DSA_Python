# Usingset
def findUnion(a, b):                         # Function to find union of two arrays

    s = set()                                # Creates an empty set to store unique elements

    for num in a:                            # Traverses each element in array a
        s.add(num)                           # Adds element to set; duplicates are ignored

    for num in b:                            # Traverses each element in array b
        s.add(num)                           # Adds element to the same set

    result = list(s)                         # Converts set into a list

    return result                            # Returns the list containing union elements


a = [1, 2, 2, 3]                             # Initializes the first array
b = [2, 3, 4, 5]                             # Initializes the second array

result = findUnion(a, b)                     # Calls the function and stores the result

print("Union:", result)                      # Prints the union of both arrays


# 2. set union operator
"""
def findUnion(a, b):
    s = set(a) | set(b)                      # Combines both sets and removes duplicates
    return list(s)                           # Converts set into list

a = [1, 2, 2, 3]
b = [2, 3, 4, 5]

print("Union:", findUnion(a, b))

"""
