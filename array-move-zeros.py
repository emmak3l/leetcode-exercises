# Move Zeros

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.


# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
 

# Follow up: Could you minimize the total number of operations done?

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# January 5th, 2024
# First Attempt
# This is my brute force attempt, the runtime is very fast but it is on the high end of memory usage for this problem.
# The first hint suggested I try to solve it without worrying about doing it in place at first, so that's whay I did.
# The second hint suggests that you can use a two pointer solution to solve this, so I will try to re-write my solution in a two-pointer format for my next attempt.
# 74 / 74 test cases passed.
# Runtime: 135 ms (Your runtime beats 86.93 % of python3 submissions.)
# Memory Usage: 18.8 MB (Your memory usage beats 15.61 % of python3 submissions.)


# class Solution:
#     def moveZeroes(self, nums: list[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         ordered = [x for x in nums if x != 0]
        
#         for x in nums:
#         	if x == 0:
#         		ordered.append(x)

#         i = 0

#         while i < len(nums):
#         	nums[i] = ordered[i]
#         	i += 1




# s = Solution()

# nums = [0,1,0,3,12]

# print(nums)

# s.moveZeroes(nums)

# print(nums)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# January 5th, 2024
# Second Attempt
# I figured out how to do the two pointer solution to this problem will a little help from google, I'm starting to get the hang of it
# This is slightly faster than my first attempt but surprisingly uses the same amount of memory.
# I looked at more efficent memory solutions and they're all variations on this solution so I'm not sure if there's any significant memory improvements I could make to this.
# 74 / 74 test cases passed.
# Runtime: 131 ms (Your runtime beats 91.05 % of python3 submissions.)
# Memory Usage: 18.9 MB (Your memory usage beats 15.61 % of python3 submissions.)

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        j = 0  
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1 

s = Solution()

nums = [0,1,0,3,12]

print(nums)

s.moveZeroes(nums)

print(nums)