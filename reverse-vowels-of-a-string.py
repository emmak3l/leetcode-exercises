# Reverse Vowels of a String

# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"
 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# February 29th, 2024
# First Attempt
# This is my initial brute force solution using a two pointer approach.
# I convert s to a list and compare each index to the vowels set, swapping positions when both pointers are vowels
# This solution has a very fast runtime and very good memory usage compared to other python3 submissions
# All test cases passed
# Runtime: 40ms (Beats 93.32% of users with Python3)
# Memory: 17.46 MB (Beats 84.19% of users with Python3)

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','A','e','E','i','I','o','O','u','U'}
        sList = list(s)
        i = 0
        j = len(s) - 1

        while i < j:
        	if sList[i] not in vowels:
        		i += 1
        	if sList[j] not in vowels:
        		j -= 1
        	if sList[i] in vowels and sList[j] in vowels:
        		sList[i], sList[j] = sList[j], sList[i]
        		i += 1
        		j -= 1

        result = "".join(sList)

        return result

sol = Solution()
s = "hello"
print(sol.reverseVowels(s))