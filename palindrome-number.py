# Palindrome Number

# Given an integer x, return true if x is a palindrome, and false otherwise.
 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
# Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1
 

# Follow up: Could you solve it without converting the integer to a string?

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# February 9th, 2024
# First Attempt
# I have solved palindrome questions in the past and implemented a very simple and clean two-pointer solution here
# It has a very fast runtime and excellent memory usage compared to other submissions
# All test cases passed
# Runtime: 43ms (Beats 94.42% of users with Python3)
# Memory: 16.59 MB (Beats 73.48% of users with Python3)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        i = 0
        j = len(num) - 1

        while i < j:
        	if num[i] != num[j]:
        		return False
        	i += 1
        	j -= 1

        return True

sol = Solution()

print(sol.isPalindrome(101))