n=int(input("enter n value"))
l=list(map(int,input().split())) # Instead of list(map()) directly we can use the for loop to enter the values into it.
i,j=0,n-1
while(i<=j):
  l[i],l[j]=l[j],l[i]
  i+=1
  j-=1
print(l)

"""
# Python Notes: Reverse a List Using Two Pointers

## Code

```python
n = int(input("Enter n value: "))
l = list(map(int, input().split()))

i, j = 0, n

while i <= j:
    l[i], l[j] = l[j], l[i]
    i += 1
    j -= 1

print(l)
```

## Line-by-Line Notes

### 1. Read the number of elements

```python
n = int(input("Enter n value: "))
```

- `input()` reads input from the user as a string.
- `int()` converts the input string into an integer.
- `n` stores the number entered by the user.

### 2. Read list elements

```python
l = list(map(int, input().split()))
```

- `input()` reads the elements entered on one line.
- `split()` separates the input using whitespace.
- `map(int, ...)` converts each element into an integer.
- `list()` converts the mapped values into a list.
- `l` stores all the input elements.

### 3. Initialize two pointers

```python
i, j = 0, n
```

- `i = 0` points to the first element.
- `j = n` is intended to point to the last element, but this is incorrect for a list of size `n`.
- The last valid index is `n - 1`.

Correct initialization:

```python
i, j = 0, n - 1
```

### 4. Set the loop condition

```python
while i <= j:
```

- `while` repeats the block as long as the condition is true.
- `i <= j` means the left pointer is less than or equal to the right pointer.
- For list reversal, `while i < j` is sufficient because the middle element does not need to be swapped.

### 5. Swap list elements

```python
l[i], l[j] = l[j], l[i]
```

- Swaps the values at indices `i` and `j`.
- Python allows multiple assignment, so a temporary variable is not required.
- The first element is exchanged with the last element, then the second with the second-last, and so on.

### 6. Move the pointers

```python
i += 1
```

- Increments `i` by `1`.
- Moves the left pointer toward the right.

```python
j -= 1
```

- Decrements `j` by `1`.
- Moves the right pointer toward the left.

### 7. Print the reversed list

```python
print(l)
```

- Displays the final list after reversing its elements.

## Important Correction

Use the following code to avoid an index error:

```python
n = int(input("Enter n value: "))
l = list(map(int, input().split()))

i, j = 0, len(l) - 1

while i < j:
    l[i], l[j] = l[j], l[i]
    i += 1
    j -= 1

print(l)
```

Using `len(l) - 1` ensures that `j` points to the last valid list index.

## Example

Input:

```text
5
10 20 30 40 50
```

Output:

```text
[50, 40, 30, 20, 10]
```

## Concepts to Remember

- `input()` — reads user input.
- `int()` — converts a value into an integer.
- `split()` — separates input into parts.
- `map()` — applies a function to each element.
- `list()` — creates a list.
- `len(l)` — returns the number of elements in the list.
- `l[i], l[j] = l[j], l[i]` — swaps two elements.
- Two-pointer technique — processes elements from opposite ends.
- Time complexity — `O(n)`.
- Auxiliary space complexity — `O(1)` for the reversal operation.
"""
