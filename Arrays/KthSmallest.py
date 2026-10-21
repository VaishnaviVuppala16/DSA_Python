arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter k value: "))

arr.sort()

print(arr[k - 1])
