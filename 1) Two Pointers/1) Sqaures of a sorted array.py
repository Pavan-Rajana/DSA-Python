class Solution:
    def sortedSquares(self,nums):
        left = 0
        right = len(nums) - 1
        result = []
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result.append(nums[left] ** 2)
                left =+ 1
            else:
                result.append(nums[right] ** 2)
                right -= 1
        result.reverse()

        return result
    

# Create an instance of the Solution class
solution = Solution()

# Call the sortedSquares method and pass a test list
nums = [-4, -1, 0, 3, 10]
result = solution.sortedSquares(nums)

# Print the result
print(result)
