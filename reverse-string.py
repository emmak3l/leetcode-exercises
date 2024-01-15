# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.


# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is a printable ascii character.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# January 15th, 2024
# First Attempt
# I wanted to try out a two pointer approach that I recently learned in my Udemy course, it worked and was super fast!
# 477 / 477 test cases passed.
# Runtime: 162 ms (Your runtime beats 95.14 % of python3 submissions.)
# Memory Usage: 21.6 MB (Your memory usage beats 33.67 % of python3 submissions.)

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
        	temp = s[left]
        	s[left] = s[right]
        	s[right] = temp
        	left += 1
        	right -= 1

        return s


s = ["H","a","n","n","a","h"]

print(Solution().reverseString(s))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# January 15th, 2024
# Second Attempt
# Wanted to try the built in method reverse() to test the methods performance.
# It's not as fast as my two pointer approach but it is slightly better memory usage
# 477 / 477 test cases passed. 
# Runtime: 175 ms (Your runtime beats 71.90 % of python3 submissions.)
# Memory Usage: 21.6 MB (Your memory usage beats 46.16 % of python3 submissions.)

# class Solution:
#     def reverseString(self, s: list[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         s.reverse()
#         return s




