# Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 
# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# January 19th, 2024
# First Attempt
# Used regex and lower to convert to a lowercase alphanumeric string a two pointer approach to check if it's a palindrome
# My solution is not super fast and and not super memory efficient based on the other submissions.
# Looking at the distribution graph of answers though it looks like I'm right in the middle of the bell curves, so my answer is very average.
# I think if I found a different way to convert the string to only alphanumeric chars that isn't regex that my solution would be faster.
# Looking at some of the faster solutions it looks like I could use the method isalnum() instead of regex in the future.
# 485 / 485 test cases passed.
# Runtime: 48 ms (Your runtime beats 61.25 % of python3 submissions.)
# Memory Usage: 17.9 MB (Your memory usage beats 34.97 % of python3 submissions.)

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1 = re.sub(r'[\W_]+', '', s).lower()
        if str1 == "":
        	return True
        i = 0
        j = (len(str1) - 1)
        while i < j:
        	if str1[i] == str1[j]:
        		i += 1
        		j -= 1
        	else:
        		return False
        return True

str1 = "A man, a plan, a canal: Panama"
str2 = "race a car"

sol = Solution()

print(sol.isPalindrome(str2))