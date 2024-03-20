# Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product
# of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.
 

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) extra space complexity? 
# (The output array does not count as extra space for space complexity analysis.)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# March 20th, 2024
# First Attempt
# First time in a long while that my first submission worked without any errors to fix, yay! First try B)
# This solution has an excellent runtime and great memory usage compared to other python3 submissions
# Runtime: 160ms (Beats 82.42% of users with Python3)
# Memory: 23.71 MB (Beats 74.51% of users with Python3)

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
    	output = []
    	product = 1
    	numZero = 0

    	for n in nums:
    		if n != 0:
    			product = product * n
    		if n == 0:
    			numZero += 1
    	
    	if numZero > 1:
    		return [0]*len(nums)

    	for i in range(len(nums)):
    		if numZero == 1:
    			if nums[i] != 0:
    				output.append(0)
    			else:
    				output.append(product)
    		else:
    			if nums[i] == 0:
    				output.append(0)
    			else:
    				output.append(int(product/nums[i]))

    	return output



sol = Solution()

print(sol.productExceptSelf([1,2,3,4]))        