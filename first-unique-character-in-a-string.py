# First Unique Character in a String

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.


# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only lowercase English letters.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# January 18th, 2024
# First Attempt

class Solution:
    def firstUniqChar(self, s: str) -> int:
        lookup = {}

        for letter in s:
            # if letter exists, increment, otherwise set to 1
            lookup[letter] = lookup.get(letter, 0) + 1

        for item in lookup:
        	# search for the first item that has a value of 1 in the lookup dict
        	if lookup[item] == 1:
        		# return the index of the item(unique char)
        		return s.find(item)
        
        # if no items in the lookup dict have a value of 1, then there are no unique characters and we return -1
        return -1




sol = Solution()

print(sol.firstUniqChar("llama"))