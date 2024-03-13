# Reverse Words in a String

# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. 
# The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words.
# The returned string should only have a single space separating the words. Do not include any extra spaces.


# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"

# Example 2:
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.

# Example 3:
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

# Constraints:

# 1 <= s.length <= 104
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.
 

# Follow-up: If the string data type is mutable in your language,
# can you solve it in-place with O(1) extra space?

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# March 13th, 2024
# First Attempt
# I did a very simple brute force one liner solution to start
# This solution doesn't have a fast runtime but excellent memory usage compared with other python3 submissions
# Runtime: 42ms (Beats 24.03% of users with Python3)
# Memory: 16.66 MB (Beats 83.10% of users with Python3)

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         return " ".join(s.split()[::-1])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# March 13th, 2024
# Second Attempt
# Wanted to try doing a two pointer solution and see how that would affect the runtime
# First converted the string to a list using the split() method to only grab the words and no extra whitespace
# Initialized i and j pointers and swapped the values of l[i] and l[j] while i was less than j
# Coverted the l list back to a string called result using the join method, adding a space between each word
# Returned result
# This solution has a much better runtime and slightly better memory usage than my first solution
# Runtime: 39ms (Beats 41.75% of users with Python3)
# Memory: 16.53 MB (Beats 98.62% of users with Python3)

class Solution:
    def reverseWords(self, s: str) -> str:
        l = list(s.split())
        i = 0
        j = len(l) - 1

        while i < j:
        	l[i], l[j] = l[j], l[i]
        	i += 1
        	j -= 1

        result = " ".join(l)

        return result

sol = Solution()
s = "the sky is blue"

print(sol.reverseWords(s))