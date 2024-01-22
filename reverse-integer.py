# Reverse Integer

# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:

# -2^31 <= x <= 2^31 - 1

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# January 22nd, 2024
# First Attempt
# Used a two pointer approach to solve this problem
# I could retry this with a slice method to see if it's any faster that way
# Fairly decent runtime and memory usage compared to others submissions
# 1045 / 1045 test cases passed.
# Runtime: 36 ms (Your runtime beats 75.20 % of python3 submissions.)
# Memory Usage: 16.6 MB (Your memory usage beats 54.08 % of python3 submissions.)

class Solution:
    def reverse(self, x: int) -> int:
        xlist = list(str(x))
        print(xlist)
        left = 0
        right = len(xlist) - 1

        while left < right:
            if xlist[left] == '-':
                left += 1
            xlist[left], xlist[right] = xlist[right], xlist[left]
            left += 1
            right -= 1

        output = int("".join(str(x) for x in xlist))

        if output > -2147483648 and output < 2147483647:
            return output
        else:
            return 0

sol = Solution()

print(sol.reverse(120))
