# Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# January 8th, 2024
# First Attempt
# I looked at the hints and saw that using a hashmap (dict in python) was recommended for faster performance
# This solution could be optimized into a single loop
# 61 / 61 test cases passed.
# Runtime: 60 ms (Your runtime beats 82.16 % of python3 submissions.)
# Memory Usage: 18.4 MB (Your memory usage beats 19.14 % of python3 submissions.)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
    	# initializing a blank dictionary called dictNums
        dictNums = {}

        # Populating dictNums by enumerating the nums list so values of num are the keys and the index (i) numbers are the values
        # e.g. [3,2,4] -> {3: 0, 2: 1, 4: 2}
        for i, num in enumerate(nums):
        	dictNums[num] = i

        print(dictNums)
        
        # iterate through enumerated nums
        for i, num in enumerate(nums):
        	# calculate the complement of num by subtracting it from the target
        	complement = target - num
        	# if the complement is in dictNums and it's value does not equal i, then we return the values(the corresponding nums list indices) for i and complement in a list
        	# we have to check that the value does not equal i in the event that the key of complement is the same as the key of num
        	# this way we won't return the index of num twice and will instead find the other index that matches the value of complement
        	# e.g. nums = [3,3], target = 6, dictNums = {3: 0, 3: 1}, complement = 6 - 3 = 3
        	if complement in dictNums and dictNums[complement] != i:
        		return [i, dictNums[complement]]
        # if we are unable to find values that add up to the target in the nums list then we return an empty list
        return []


s = Solution()

nums = [3,2,4]
target = 6

print(s.twoSum(nums,target))