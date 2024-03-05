# Counting Bits

# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
# ans[i] is the number of 1's in the binary representation of i.
 

# Example 1:
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

# Example 2:
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
 

# Constraints:

# 0 <= n <= 105

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# March 5th, 2024
# First Attempt
# My first brute force solution using a for loop with the format() and count() methods
# This has a poor runtime and decent memory usage compared with other ptyhon3 submissions
# All test cases passed
# Runtime: 65ms (Beats 36.50% of users with Python3)
# Memory: 15.64 MB (Beats 47.42% of users with Python3)

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []

        for i in range(n+1):
        	result.append(str(format(i, 'b')).count("1"))
        
        return result

sol = Solution()

print(sol.countBits(5))