# Length of Last Word

# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

 
# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# February 22th, 2024
# First Attempt
# First I elminated all the leading white spaces, then I incremented the count until encountering another white space
# This solution is extremely fast and has excellent memory usage
# All test cases passed
# Runtime: 28ms (Beats 92.60% of users with Python3)
# Memory: 16.52 MB (Beats 90.26% of users with Python3)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        i = len(s) - 1

        while s[i] == " ":
        	i -= 1
        while i >= 0:
        	if s[i] != " ":
        		count += 1
        		i -= 1
        	else:
        		break

        return count


sol = Solution()

print(sol.lengthOfLastWord("luffy is still joyboy"))
