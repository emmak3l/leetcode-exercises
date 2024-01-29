# Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# January 29th, 2024
# First Attempt
# I could not for the life of me figure out how to do this without looking up solutions unfortunately
# Below is what I tried and although it worked for the two example cases in the description it could not pass all the test cases
# I thought it would be valuable for me to upload my thought process regardless so I can compare to other solutions

# *** NOTE THAT THIS DOES NOT WORK ***
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
    	prefix = min(strs, key=lambda n: len(n))
    	if len(prefix) == 0:
    		return ""
    	compare = [x for x in strs if x != prefix]
    	print(prefix)
    	print(compare)
    	i = 0
    	j = 0

    	while j <= len(compare) - 1:
    		if i == len(prefix):
    			j += 1
    			i = 0
    			print(i,j)
    		if prefix[i] == compare[j][i]:
    			i += 1
    			print(i,j)
    		else:
    			prefix = prefix[0:i]
    			print(prefix)
    			print("len: ", len(prefix))
    			print(i,j)
    			if len(prefix) == 0:
    					return ""
    			j += 1
    			i = 0
    			print(i,j)

    	return prefix

sol = Solution()

print(sol.longestCommonPrefix(["flower","flow","flight"]))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# January 29th, 2024
# A Solution I found Online
# This is one possible solution of many that I found online
# I will come back at another time to explore other solutions to this problem in the future
# 124 / 124 test cases passed.
# Runtime: 45 ms (Your runtime beats 29.02 % of python3 submissions.)
# Memory Usage: 16.5 MB (Your memory usage beats 77.17 % of python3 submissions)

# class Solution:
#     def longestCommonPrefix(self, strs: list[str]) -> str:
#         if not strs:
#             return ""
#         for i, letter_group in enumerate(zip(*strs)):
#             if len(set(letter_group)) > 1:
#                 return strs[0][:i]
#         else:
#             return min(strs)
