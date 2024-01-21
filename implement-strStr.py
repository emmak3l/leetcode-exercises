# Implement strStr()

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
#  or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# January 21th, 2024
# First Attempt
# Decided to do a brute force solution to start
# Not very fast or memory efficient compared to other solutions but not the worst
# For my next attempt I'll figure out how to implement a sliding window approach
# 82 / 82 test cases passed.
# Runtime: 37 ms (Your runtime beats 61.37 % of python3 submissions.)
# Memory Usage: 16.5 MB (Your memory usage beats 58.55 % of python3 submissions.)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
        	return haystack.index(needle)
        else:
        	return -1

s = Solution()
haystack = "butsadsad"
needle = "sad"


print(s.strStr(haystack,needle))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# January 21th, 2024
# Second Attempt
# Used sliding window approach with slices for this solution which significantly increased the runtime performance.
# 82 / 82 test cases passed.
# Runtime: 30 ms (Your runtime beats 92.90 % of python3 submissions.)
# Memory Usage: 16.5 MB (Your memory usage beats 56.37 % of python3 submissions.)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        if n > len(haystack):
            return -1
        else:
            for i in range(len(haystack) - n+1):
                temp = haystack[i:i+n]
                if needle == temp:
                    return i
        return -1