def negEnd(arr):                  # Defines a function that moves negative elements to the end
    n = len(arr)                  # Gets the total number of elements in the array
    a = []                        # Creates an empty list to store rearranged elements
    j = 0                         # Initializes an index variable (not required when using append)
    # Store positive and zero elements
    for i in range(n):            # Iterates through the original array from index 0 to n-1
        if arr[i] >= 0:            # Checks whether the current element is positive or zero
            a.append(arr[i])       # Adds the element to the end of the temporary list to preserve order
    # Store negative elements
    for i in range(n):            # Iterates through the original array again
        if arr[i] < 0:             # Checks whether the current element is negative
            a.append(arr[i])       # Adds the negative element after all positive elements
    # Copy elements back to original array
    for i in range(n):             # Iterates through all indices of the original array
        arr[i] = a[i]              # Copies each rearranged element back to the original array
    return arr                     # Returns the modified array as the function output
arr = list(map(int, input().split()))  # Takes space-separated integers and converts them into a list
print(negEnd(arr))                 # Calls the function and prints the rearranged array
      
