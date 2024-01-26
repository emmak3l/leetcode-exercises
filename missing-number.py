# Missing Number

# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.

 

# Example 1:

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
#			   2 is the missing number in the range since it does not appear in nums.
# Example 2:

# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2].
#			   2 is the missing number in the range since it does not appear in nums.
# Example 3:

# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9].
#			   8 is the missing number in the range since it does not appear in nums.
 

# Constraints:

# n == nums.length
# 1 <= n <= 104
# 0 <= nums[i] <= n
# All the numbers of nums are unique.
 

# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# January 26th, 2024
# First Attempt
# This was my first brute force attempt using list comprehension
# It's incredibly slow but decently memory efficient
# 122 / 122 test cases passed.
# Runtime: 2122 ms
# Memory Usage: 17.9 MB (Your memory usage beats 64.93 % of python3 submissions.)

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        new = list(range(0,len(nums)+1))
        
        return [x for x in new if x not in nums][0]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# January 26th, 2024
# Second Attempt
# For my second attempt instead of creating a brand new list to compare against using list comprehension like in the first solution
# I sorted the nums list then compared i to the range of the length of the nums list, if i isn't in nums then it's the missing number and is returned
# 122 / 122 test cases passed.
# Runtime: 134 ms (Your runtime beats 28.29 % of python3 submissions.)
# Memory Usage: 17.8 MB (Your memory usage beats 80.11 % of python3 submissions.)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i]!=i:
                return i
        return len(nums)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# January 26th, 2024
# Solution I found on the Submissions Page
# This solution was clean and elegant and I wanted to save it for future reference
# It's faster than my previous two solutions but less memory efficient
# 122 / 122 test cases passed.
# Runtime: 116 ms (Your runtime beats 66.95 % of python3 submissions.)
# Memory Usage: 18.5 MB (Your memory usage beats 36.58 % of python3 submissions.)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        for i in range(len(nums)+1):
            if i not in nums:
                return i