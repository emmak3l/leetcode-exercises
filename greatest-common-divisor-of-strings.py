# The Greatest Common Divisor of Strings

# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.


# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

# Example 2:
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"

# Example 3:
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
 

# Constraints:

# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# March 18th, 2024
# Neetcode Solution
# I couldn't figure this out in a reasonable amount of time so I looked up NeetCode's solution
# Runtime: 38ms (Beats 50.68% of users with Python3)
# Memory: 16.65 MB (Beats 29.29% of users with Python3)

# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         len1, len2 = len(str1), len(str2)

#         def isDivisor(l):
#             if len1 % l or len2 % l:
#                 return False
#             f1, f2 = len1 // l, len2 // l
#             return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

#         for l in range(min(len1,len2), 0, -1):
#             if isDivisor(l):
#                 return str1[:l]
#         return ""
        

sol = Solution()

print(sol.gcdOfStrings("LEET", "CODE"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# March 18th, 2024
# LeetCode Submission Code Sample
# I found this solution on the submission page and really liked how clean and simple it was, saving it for future reference
# Runtime: 38ms (Beats 50.68% of users with Python3)
# Memory: 16.57 MB (Beats 70.26% of users with Python3)

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if they have non-zero GCD string.
        if str1 + str2 != str2 + str1:
            return ""

        # Get the GCD of the two lengths.
        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]
