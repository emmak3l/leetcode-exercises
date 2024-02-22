# Add Binary

# Given two binary strings a and b, return their sum as a binary string.


# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# February 20th, 2024
# First Attempt
# I used pythons built in methods to solve this problem.
# This solution has a very fast runtime and excellent memory usage
# All test cases passed
# Runtime: 34ms (Beats 81.57% of users with Python3)
# Memory: 16.46 MB (Beats 98.04% of users with Python3)

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = str(bin((int(a, 2) + int(b, 2))))

        return result[2::]

sol = Solution()

print(sol.addBinary("11","1"))