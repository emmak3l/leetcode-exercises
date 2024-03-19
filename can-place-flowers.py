# Can Place Flowers

# You have a long flowerbed in which some of the plots are planted, and some are not. 
# However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
# and an integer n, return true if n new flowers can be planted in the flowerbed without 
# violating the no-adjacent-flowers rule and false otherwise.
 

# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
 

# Constraints:

# 1 <= flowerbed.length <= 2 * 104
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# March 19th, 2024
# First Attempt
# I thought I could solve this with a sliding window approach but it didn't work for the edge case tests

# class Solution:
#     def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
#     	minSum = 0
#     	tempSum = 0
#     	window = n + n + 1

#     	for i in range(window):
#     		minSum += flowerbed[i]

#     	tempSum = minSum
#     	i = window

#     	while i < len(flowerbed):
#     		tempSum = tempSum - flowerbed[i-window] + flowerbed[i]
#     		minSum = min(minSum, tempSum)
#     		i += 1

#     	if minSum < n: 
#     		return True

#     	return False

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# March 19th, 2024
# NeetCode Assistance
# I watched the first half of NeetCodes video solution to this problem to point me in the right direction
# I did not watch the coding portion though just the problem explanation, all the code below is my own
# This solution has a decently fast runtime and okay memory usage compared to other python3 submissions
# Runtime: 129ms (Beats 71.84% of users with Python3)
# Memory: 16.96 MB (Beats 35.96% of users with Python3)

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
    	newFlowerbed = [0] + flowerbed + [0]
    	i = 1
    	count = 0

    	while i < len(flowerbed)+ 1:
    		if newFlowerbed[i-1] == 0 and newFlowerbed[i] == 0 and newFlowerbed[i+1] == 0:
    			count += 1
    			i += 1
    		i += 1

    	if count >= n:
    		return True

    	return False

sol = Solution()

print(sol.canPlaceFlowers([1,0,0,0,0,1], 2))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# March 19th, 2024
# NeetCode's Solution
# I wanted to see how NeetCode's solution compared to mine so his is below
# Our solutions are so similar in runtime and memory usage which is nice!
# Runtime: 128ms (Beats 76.31% of users with Python3)
# Memory: 17.00 MB (Beats 35.96% of users with Python3)


# class Solution:
#     def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
#     	f = [0] + flowerbed + [0]

#     	for i in range(1, len(f) - 1):
#     		if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
#     			f[i] = 1
#     			n -= 1

#     	return n <= 0


