# Maximum Number of Vowels in a Substring of Given Length

# Given a string s and an integer k, return the maximum number of vowel letters 
# in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.
# 1 <= k <= s.length

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# March 25th, 2024
# First Attempt
# My first submission attempt was accepted yay! I used a simple sliding window solution to solve this problem
# This solution has a good runtime and memory usage compared to other python3 submissions
# Runtime: 119ms (Beats 63.02% of users with Python3)
# Memory: 17.28 MB (Beats 63.95% of users with Python3)

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        maxNum = 0
        tempNum = 0

        if len(s) == 1:
        	if s in vowels:
        		return 1
        	else:
        		return 0

        for i in range(k):
        	if s[i] in vowels:
        		maxNum += 1

        tempNum = maxNum

        i = k

        while i < len(s):
        	if s[i-k] in vowels:
        			tempNum -= 1
        	if s[i] in vowels:
        		tempNum += 1
        	maxNum = max(maxNum, tempNum)
        	i += 1

        return maxNum


sol = Solution()

print(sol.maxVowels("abciiiedef", 6))





