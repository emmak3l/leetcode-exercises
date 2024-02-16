# Contains Duplicate II

# Given an integer array nums and an integer k, return true if there are two distinct indices
# i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.


# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 0 <= k <= 105

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# February 16th, 2024
# First Attempt
# I couldn't solve this in a reasonable amount of time so I looked up Neetcodes solution, which is below
# This solution has a very fast runtime and excellent memory efficiency
# All test cases passed
# Runtime: 455ms (Beats 84.02% of users with Python3)
# Memory: 28.02 MB (Beats 91.16% of users with Python3)

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
    	window = set()
    	l = 0

    	for r in range(len(nums)):
    		if r - l > k:
    			window.remove(nums[l])
    			l += 1
    		if nums[r] in window:
    			return True
    		window.add(nums[r])
    	return False

sol = Solution()

print(sol.containsNearbyDuplicate([1,2,3,1,2,3], 2))