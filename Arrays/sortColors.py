#                   Dutch National Flag algorithm (3-pointers approach)

def sort(arr):                     # Function to sort the array containing 0s, 1s, and 2s
    l, m = 0, 0                    # l = position for 0s, m = current element index
    h = len(arr) - 1               # h = position for 2s (last index)

    while m <= h:                  # Continue until the pointers cross
        if arr[m] == 0:            # If the current element is 0
            arr[l], arr[m] = arr[m], arr[l]  # Swap current element with arr[l]
            l += 1                 # Move the 0s pointer forward
            m += 1                 # Move to the next element

        elif arr[m] == 1:           # If the current element is 1
            m += 1                 # 1 is already in the correct region

        else:                      # If the current element is 2
            arr[m], arr[h] = arr[h], arr[m]  # Swap with the element at the end
            h -= 1                 # Move the 2s pointer backward
                                     # Do not increment m; check the swapped element

    return arr                     # Return the sorted array


arr = list(map(int, input().split()))  # Read space-separated integers into a list
print(sort(arr))                        # Sort the array and print the result
