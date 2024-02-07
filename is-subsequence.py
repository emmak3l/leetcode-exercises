# Is Subsequence

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some 
# (can be none) of the characters without disturbing the relative positions of the remaining characters. 
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
 

# Constraints:

# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.
 

# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109,
#  and you want to check one by one to see if t has its subsequence. 
#  In this scenario, how would you change your code?

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# February 7th, 2024
# First Attempt
# My first brute force solution using a two pointer approach, I'm going to optimize this and resubmit
# My solution isn't super fast compared to other submissions but it's decently memory efficient
# All test cases passed
# Runtime: 49ms (Beats 12.04% of users with Python3)
# Memory: 16.81 MB (Beats 55.02% of users with Python3)

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         if s == "":
#             return True
#         if t == "" and s != "":
#             return False

#         i = 0
#         j = 0

#         while j < len(t):
#             if s[i] == t[j]:
#                 i += 1
#                 j += 1
#             else:
#                 j += 1
#             if i == len(s):
#                 break

#         if i == len(s):
#             return True
#         else:
#             return False


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# February 7th, 2024
# Second Attempt
# By refactoring my code slightly I was able to significantly improve my runtime and improve my memory usage slightly
# All test cases passed
# Runtime: 34ms (Beats 73.38% of users with Python3)
# Memory: 16.81 MB (Beats 57.16% of users with Python3)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) <= 0:
            return True
        if len(t) <= 0:
            return False
            
        i = 0
        j = 0

        while j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
            if i == len(s):
                return True

        return False

sol = Solution()

print(sol.isSubsequence("b", "abc"))