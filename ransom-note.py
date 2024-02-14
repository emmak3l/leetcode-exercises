# Ransom Note

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by
#  using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true
 

# Constraints:

# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# February 14th, 2024
# First Attempt
# Used a frequency counter problem solving approach to solve this question
# The solution is very fast and decently memory efficient compared to other python3 submissions
# All test cases passed
# Runtime: 49ms (Beats 81.26% of users with Python3)
# Memory: 16.74 MB (Beats 68.77% of users with Python3)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter1 = {}
        counter2 = {}

        for letter in ransomNote:
        	counter1[letter] = counter1.get(letter, 0) + 1
        for letter in magazine:
        	counter2[letter] = counter2.get(letter, 0) + 1
        for key in counter1:
        	if key not in counter2:
        		return False
        	if counter2[key] < counter1[key]:
        		return False
        return True

sol = Solution()

print(sol.canConstruct("aa", "ab"))