# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.


# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# October 18th, 2023  (forgot to merge this to my git that day)
# First Brute Force Attempt

# This solution is incredibly slow and not optimized in the slightest. I will come back and attempt a more optimized solution in the future.
# 61/61 test cases passed.
# Runtime: 4395 ms (Your runtime beats 8.61 % of python3 submissions.)
# Memory Usage: 18.9 MB (Your memory usage beats 59.65 % of python3 submissions.)

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for num in nums:
            if nums.count(num) == 1:
                return num

sol = Solution()
print(sol.singleNumber([2,2,1])) # 1
print(sol.singleNumber([4,1,2,1,2])) # 4
print(sol.singleNumber([1])) # 1