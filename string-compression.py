# String Compression

# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input 
# character array chars. Note that group lengths that are 10 or longer will be split into
# multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.

 

# Example 1:
# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

# Example 2:
# Input: chars = ["a"]
# Output: Return 1, and the first character of the input array should be: ["a"]
# Explanation: The only group is "a", which remains uncompressed since it's a single character.

# Example 3:
# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
 

# Constraints:

# 1 <= chars.length <= 2000
# chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# March 6th, 2024
# First Attempt
# I tried to brute force a solution with a frequency counter and a bunch of for loops
# but couldn't make it work for all test cases, failed at ["a","a","a","b","b","a","a"]:
# output was ["a","5","b","2"] (cause of the frequency counter) but they expected ["a","3","b","2","a","2"]
# I think I have to use a two pointer approach instead of a frequency counter based on this test case
# but I've already worked on this for an hour and don't want to spend more time trying to solve on my own
# Will post a working solution I looked up below this

# class Solution:
#     def compress(self, chars: list[str]) -> int:
#         result = []
#         frequency_counter = {}

#         for val in chars:
#         	frequency_counter[val] = frequency_counter.get(val, 0) + 1

#         for key, val in frequency_counter.items():
#         	result.extend([key,str(val)])

#         for i in range(len(result)-1):
#         	if result[i] == '1':
#         		result.pop(i)

#         if len(result) == 2:
#         	for i in range(len(result)):
#         		if result[i] == '1':
#         			result.pop(i)

#         for i in range(len(result)):
#         	if len(result[i]) > 1:
#         		for num in result[i]:
#         			result.append(num)
#         		result.pop(i)

#         chars.clear()

#         for i in range(len(result)):
#         	chars.append(result[i])

#         return len(result), chars

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# March 6th, 2024
# Lit Code's Solution
# I looked up a solution to this problem on YouTube so I would understand how to implement it
# All test cases passed
# Runtime: 54ms (Beats 82.16% of users with Python3)
# Memory: 16.90 MB (Beats 29.55% of users with Python3)

class Solution:
    def compress(self, chars: list[str]) -> int:
    	num_chars = len(chars)

    	if num_chars < 2:
    		return num_chars

    	i = 0
    	j = 0

    	while i < num_chars:
    		count = 1

    		while i < num_chars - 1 and chars[i] == chars[i+1]:
    			count += 1
    			i += 1

    		chars[j] = chars[i]
    		j += 1

    		if count > 1:
    			for val in str(count):
    				chars[j] = val
    				j += 1
    		i += 1

    	return j

sol = Solution()

print(sol.compress(["a"]))


