# Power of Three

# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3x.
 

# Example 1:

# Input: n = 27
# Output: true
# Explanation: 27 = 33
# Example 2:

# Input: n = 0
# Output: false
# Explanation: There is no x where 3x = 0.
# Example 3:

# Input: n = -1
# Output: false
# Explanation: There is no x where 3x = (-1).
 

# Constraints:

# -231 <= n <= 231 - 1

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# January 25th, 2024
# First Attempt
# This was the most straightforward solution I could think of that has a fast runtime and fairly good memory usage
# 21040 / 21040 test cases passed.
# Runtime: 57 ms (Your runtime beats 91.87 % of python3 submissions.)
# Memory Usage: 16.6 MB (Your memory usage beats 59.47 % of python3 submissions.)

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
    	# if n is less than 1 we return False
    	if n < 1:
    		return False
    	# while n % 3 equals 0, we iteratively divide by 3 until in no longer equals 0
    	while (n % 3 == 0):
    		n /= 3
    	# if n is a multiple of 3, the result of the while loop will be 1.0 which is equal to 1 so it will return True
    	# if n is divisible by 3 but not a multiple, the result of the while loop will not be 1 so it will return False
    	return n == 1;

sol = Solution()

print(sol.isPowerOfThree(15))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# January 25th, 2024
# Recursive Solution I found on the Submissions Page
# I thought there would be a recursive solution to this problem but I couldn't think of it in the moment
# I saw this solution on the submissions page and wanted to save it for future reference
# Interestingly, this solution is much slower than my initial solution but is slightly more memory efficent
# 21040 / 21040 test cases passed.
# Runtime: 84 ms (Your runtime beats 32.73 % of python3 submissions.)
# Memory Usage: 16.4 MB (Your memory usage beats 62.48 % of python3 submissions.)

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        elif n < 1:
            return False
        else:
            return self.isPowerOfThree(n/3)