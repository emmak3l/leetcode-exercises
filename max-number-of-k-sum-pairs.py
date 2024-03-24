# Max Number of K-Sum Pairs

# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

# Return the maximum number of operations you can perform on the array.


# Example 1:

# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.

# Example 2:

# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= k <= 109

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# March 24th, 2024
# First Attempt
# This solution worked for some test cases but not all
# Couldn't figure this out in a reasonable amount of time so I looked up a solution which is posted below

# class Solution:
#     def maxOperations(self, nums: list[int], k: int) -> int:
#         result = 0
#         i = 0
#         j = len(nums) - 1

#         while i < j:
#         	if nums[i] + nums[j] == k:
#         		result += 1
#         		i += 1
#         		j -= 1
#         	elif nums[i] > k:
#         		i += 1
#         	elif nums[j] > k:
#         		j -= 1
#         	else:
#         		j -= 1

#         return result

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# March 24th, 2024
# Timothy H Chang Youtube Solution
# This solution has okay runtime and not great memory usage compared to other python3 submissions
# I don't love the way he solved this but I just wanted to find a solution to it
# Runtime: 498ms (Beats 52.42% of users with Python3)
# Memory: 29.74 MB (Beats 19.15% of users with Python3)

# from collections import Counter

# class Solution:
#     def maxOperations(self, nums: list[int], k: int) -> int:
#     	c = Counter(nums)
#     	output = 0
#     	seen = set()

#     	for x in c:
#     		if x not in seen and (k-x) in c:
#     			if x == (k-x):
#     				output += c[x]//2
#     			else:
#     				output += min(c[x],c[k-x])
#     			seen.add(x)
#     			seen.add(k-x)

#     	return output

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# March 24th, 2024
# Second Attempt
# I found another solution on the solutions page that was super similar to mine, so I tweaked my first solution so it works
# I was sooo close to solving this on my own
# This solution has an okay runtime and great memory usage compared to other python3 submissions
# Runtime: 498ms (Beats 52.42% of users with Python3)
# Memory: 29.74 MB (Beats 19.15% of users with Python3)

class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        result = 0
        i = 0
        j = len(nums) - 1

        while i < j:
        	if nums[i] + nums[j] == k:
        		result += 1
        		i += 1
        		j -= 1
        	elif nums[i] + nums[j] > k:
        		j -= 1
        	else:
        		i += 1

        return result

sol = Solution()

print(sol.maxOperations([1,2,3,4], 5))
