# Greedy Solution - locally calculating the results and passing to the further ones to get final answer. no going back in greedy.
class MinHeights:
    def getMinDiff(self, arr, k):

        arr.sort()  # Sort the tower heights in ascending order

        n = len(arr)  # Find the total number of towers

        if n == 1:
            return 0  # If only one tower, difference is 0

        ans = arr[n-1] - arr[0]  # Initially calculate maximum difference

        small = arr[0] + k  # Increase the smallest tower by k

        big = arr[n-1] - k  # Decrease the largest tower by k

        for i in range(1, n):  # Check every possible split position

            if arr[i] - k < 0:  # Check whether decreasing makes height negative
                continue  # Skip this position if height becomes negative

            mini = min(small, arr[i] - k)  # Find the minimum modified height   , current tower should be decreased

            maxi = max(big, arr[i-1] + k)  # Find the maximum modified height   , previous of the curent tower should be increased.

            ans = min(ans, maxi - mini)  # Update the minimum difference , find the ans for ans and also the current mini and maxi things.

        return ans  # Return the minimum possible difference


# ---------------- DRIVER CODE ----------------

k = 2  # Value to increase or decrease each tower

arr = [1, 5, 8, 10]  # Given tower heights

obj =  MinHeights()  # Create an object of Solution class

result = obj.getMinDiff(arr, k)  # Call the method

print("Minimum difference:", result)  # Print the final answer
