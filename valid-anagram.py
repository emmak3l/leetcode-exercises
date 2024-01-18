# Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.


# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# January 18th, 2024
# First Attempt
# I solved a similar problem in my Javascript Data Structures and Algorithms Udemy course, so I converted my solution in Javascript to Python here. 
# It's fairly fast but uses a bit of memory because of the dict lookup value.
# 43 / 43 test cases passed.
# Runtime: 48 ms (Your runtime beats 75.65 % of python3 submissions.)
# Memory Usage: 17.8 MB (Your memory usage beats 26.43 % of python3 submissions.)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
        	return False

        lookup = {}

        for letter in s:
            # if letter exists, increment, otherwise set to 1
            lookup[letter] = lookup.get(letter, 0) + 1

        for letter in t:
            # can't find letter or letter is zero then it's not an anagram
            if not lookup.get(letter, 0):
                return False
            else:
                lookup[letter] -= 1

        return True

sol = Solution()

print(sol.isAnagram('cat', 'tac'))