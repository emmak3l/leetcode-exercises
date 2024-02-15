# Majority Element

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
 

# Follow-up: Could you solve the problem in linear time and in O(1) space?

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# February 15th, 2024
# First Attempt
# My first brute force solution using a frequency counter.
# I can drastically simplify this which is what I'll do for my second solution
# This solution has an average runtime and excellent memory usage
# All test cases passed
# Runtime: 136ms (Beats 53.62% of users with Python3)
# Memory: 16.74 MB (Beats 97.20% of users with Python3)

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counter = {}
        result = 0
        count = 0

        for num in nums:
        	counter[num] = counter.get(num, 0) + 1

        for key in counter:
        	if counter[key] > count:
        		result = key
        		count = counter[key]

        return result


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# February 15th, 2024
# Second Attempt
# Simplified version of my first solution
# Interestingly the runtime and memory usage is worse for this simplified version compared to my first attempt
# All test cases passed
# Runtime: 143ms (Beats 25.94% of users with Python3)
# Memory: 16.74 MB (Beats 82.18% of users with Python3)

# class Solution:
#     def majorityElement(self, nums: list[int]) -> int:
#         counter = {}

#         for num in nums:
#         	counter[num] = counter.get(num, 0) + 1

#         for key in counter:
#         	if counter[key] > len(nums) / 2:
#         		return key
        

sol = Solution()

print(sol.majorityElement([2,2,1,1,1,2,2]))