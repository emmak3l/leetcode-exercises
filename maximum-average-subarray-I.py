# Maximum Average Subarray I

# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
# Any answer with a calculation error less than 10-5 will be accepted.

 

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000
 

# Constraints:

# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# March 1st, 2024
# First Attempt
# This is a simple sliding window solution
# At first I was tripped up with the average but then I realized that if I just find the maximum sum of the
# nums list subarray then I can divide it by k at the very end to get the correct maximum average
# This solution has a great runtime and decent memory usage
# All test cases passed
# Runtime: 884ms (Beats 74.25% of users with Python3)
# Memory: 28.47 MB (Beats 62.15% of users with Python3)

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
    	maxSum = 0
    	tempSum = 0

    	for i in range(k):
    		maxSum += nums[i]

    	tempSum = maxSum

    	for i in range(k, len(nums)):
    		tempSum = tempSum - nums[i-k] + nums[i]
    		maxSum = max(maxSum,tempSum)

    	return maxSum / k

sol = Solution()

print(sol.findMaxAverage([3,3,4,3,0],3))

