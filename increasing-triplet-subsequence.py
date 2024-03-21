# Increasing Triplet Subsequence

# Given an integer array nums, return true if there exists a triple of indices (i, j, k)
# such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

# Example 1:
# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.

# Example 2:
# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.

# Example 3:
# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

# Constraints:

# 1 <= nums.length <= 5 * 105
# -231 <= nums[i] <= 231 - 1
 

# Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# March 21st, 2024
# First Attempt
# This solution works for consecutive triplets, but not non-consecutive triplets
# I misread the question they're not looking for consecutive triplets unfortunately
# [20,100,10,12,5,13] should return True because of 10,12,13
# [1,5,0,4,1,3]

# class Solution:
#     def increasingTriplet(self, nums: list[int]) -> bool:
#         i = 1

#         while i+1 < len(nums):
#         	if nums[i-1] < nums[i] < nums[i+1]:
#         		return True
#         	i += 1

#         return False

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# March 21st, 2024
# First Attempt
# I couldn't solve this problem on my own within a reasonable amount of time, but I wanted to save the work I tried

# class Solution:
#     def increasingTriplet(self, nums: list[int]) -> bool:
#         i = 0
#         j = 1
#         k = 2
#         maxNum = max(nums)

#         while k < len(nums):
#         	print(nums[i])
#         	print(nums[j])
#         	print(nums[k])
#         	print("--------")
#         	if nums[i] < nums[j] < nums[k]:
#         		return True
#         	if nums[j] == maxNum and nums[i] > nums[k]:
#         		print("first if")
#         		i += 1
#         		j += 1
#         		k += 1
#         	elif nums[i] < nums[j] and nums[j] > nums[k] and nums[i] < nums[k]:
#         		print("second if")
#         		j = k
#         		k += 1
#         	elif nums[i] < nums[j] and nums[j] > nums[k]:
#         		print("third if")
#         		k += 1
#         	else:
#         		print("four if")
#         		i += 1
#         		j += 1
#         		k += 1

#         return False

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# March 21st, 2024
# AI Learning Corner Youtube Solution
# I looked up the solution so I know how to solve it in the future
# This solution has a poor runtime but excellent memory usage compared to other python3 submissions
# Runtime: 829ms (Beats 26.01% of users with Python3)
# Memory: 32.50 MB (Beats 96.25% of users with Python3)

class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
    	n = len(nums)

    	if n < 3:
    		return False

    	left, mid = float("inf"), float("inf")

    	for i in range(n):
    		if nums[i] > mid:
    			return True
    		if nums[i] < left:
    			left = nums[i]
    		elif nums[i] > left and nums[i] < mid:
    			mid = nums[i]

    	return False



    	


sol = Solution()

print(sol.increasingTriplet([5,1,5,5,2,5,4]))


