# Rotate Array

# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
 

# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105
 

# Follow up:

# Try to come up with as many solutions as you can. 
# There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# January 31st, 2024
# First Attempt
# I could not quite figure out how to do this on my own so I watched a NeetCode video that explained it
# This is his solution, it has a very fast runtime and is decently memory efficent
# I'm going to re-work this solution to eliminate the repetition by creating a helper function
# 38 / 38 test cases passed.
# Runtime: 155 ms (Your runtime beats 85.97 % of python3 submissions.)
# Memory Usage: 28.2 MB (Your memory usage beats 56.24 % of python3 submissions.)

# class Solution:
#     def rotate(self, nums: list[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         k = k % len(nums)
#         left = 0
#         right = len(nums) - 1

#         while left < right:
#         	nums[left], nums[right] = nums[right], nums[left]
#         	left += 1
#         	right -= 1

#         left = 0
#         right = k - 1

#         while left < right:
#         	nums[left], nums[right] = nums[right], nums[left]
#         	left += 1
#         	right -= 1

#         left = k
#         right = len(nums) - 1

#         while left < right:
#         	nums[left], nums[right] = nums[right], nums[left]
#         	left += 1
#         	right -= 1

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# January 31st, 2024
# Second Attempt
# Refactored the code above to eliminate the repetition and make the final solution dry
# The runtime is slightly slower but the memory usage is slightly better than the previous solution
# 38 / 38 test cases passed.
# Runtime: 161 ms (Your runtime beats 72.36% of python3 submissions)
# Memory Usage: 28 (Your memory usage beats 61.73 % of python3 submissions.)

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        left = 0
        right = len(nums) - 1

        def reverse(left, right):
        	while left < right:
        		nums[left], nums[right] = nums[right], nums[left]
        		left += 1
        		right -= 1

        reverse(left,right)

        left = 0
        right = k - 1

        reverse(left,right)

        left = k
        right = len(nums) - 1

        reverse(left,right)

sol = Solution()

print(sol.rotate([1,2,3,4,5,6,7], 3))