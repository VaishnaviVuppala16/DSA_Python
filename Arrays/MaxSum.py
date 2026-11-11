# Kadane's algorithm
def MaxSum(arr, n):                       # Function to find maximum subarray sum
    cs = 0                               # Stores the current subarray sum
    ms = float('-inf')                   # Stores the maximum subarray sum

    for i in arr:                        # Traverse through each element in the array
        cs = cs + i                      # Add the current element to the current sum

        ms = max(cs, ms)                 # Update maximum sum if current sum is greater

        if cs < 0:                       # Check if current sum becomes negative
            cs = 0                       # Reset current sum to zero

    return ms                            # Return the maximum subarray sum


n = int(input())                         # Read the size of the array

arr = list(map(int, input().split()))[:n] # Read n space-separated integers and store them in a list

print(MaxSum(arr, n))                    # Call the function and print the maximum subarray sum
