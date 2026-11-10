def RotateByOne(arr, i, j):  # Function to reverse the array between indexes i and j
    while i <= j:  # Continue until the two pointers cross
        arr[i], arr[j] = arr[j], arr[i]  # Swap the elements at i and j
        i += 1  # Move the left pointer forward
        j -= 1  # Move the right pointer backward

n = int(input())  # Read the number of elements

arr = list(map(int, input().split()))[:n]  # Read array elements and take only the first n elements otherwise to get only n elements we should use loop to append list elements

RotateByOne(arr, 0, n-1)  # Reverse the entire array
RotateByOne(arr, 1, n-1)  # Reverse the array from index 1 to n-1

print(arr)  # Print the array after rotating right by one position
