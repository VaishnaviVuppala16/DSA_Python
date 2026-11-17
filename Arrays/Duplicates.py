
class Solution:

    def findDuplicate(self, nums):

        n = len(nums) - 1  # Get maximum number (array length - 1)

        total = 0  # Initialize sum

        for i in range(0, n + 1):  # Traverse the array

            total = total + nums[i]  # Add each element to sum

        res = (n * (n + 1)) // 2  # Expected sum from 1 to n

        return total - res  # Return duplicate number


# Driver Code
if __name__ == "__main__":

    nums = [1, 3, 4, 2, 2]  # Input array

    obj = Solution()  # Create Solution object

    result = obj.findDuplicate(nums)  # Call the method

    print(result)  # Print duplicate number

