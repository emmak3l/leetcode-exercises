# 1768. Merge Strings Alternately

# You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
 

# Constraints:

# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# September 26th, 2023
# This is my first brute force solution that has yet to be optimized. (I will create a more optimized solution at a later date)
# As is the Runtime is currently 42ms (beats 30.74% of users with Python3)
# And the Memory is currently 16.42mb (beats 27.76% of users with Python3)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Check if the both strings are the same length
        if len(word1) == len(word2):
        	# Using the zip() function to alternate the order of the strings, then joining the resulting tuple's into strings, then joining the two strings into the final string
	        return(''.join(''.join(x) for x in (zip(word1,word2))))
	    # Check if word2 is longer than word1
        elif len(word1) < len(word2):
        	# Create a variable to hold the slice of word2 which is the same length of word1
	        slice_to_zip = word2[:len(word1)]
	        # Create a variable to hold the slice of word2 that is left over
	        slice_to_append = word2[len(word1):]
	        # Create a list that contains word1 and slice_to_zip(word2 that's the same length as word1) zipped together
	        first_zip = list(zip(word1, slice_to_zip))
	        # Append the slice_to_append to the end of the list
	        first_zip.append(slice_to_append)
	        # Join all the variables into a list using list comprehension
	        first_join = [''.join(s) for s in first_zip]
	        # Finally join everything one final time to get the merged string
	        return(''.join(first_join))
	    # The else covers if word1 is longer than word2
        else:
        	# Create a variable to hold the slice of word1 which is the same length of word2
	        slice_to_zip = word1[:len(word2)]
	        # Create a variable to hold the slice of word2 that is left over
	        slice_to_append = word1[len(word2):]
	        # Create a list that contains slice_to_zip(word1 that's the same length as word2) and word2 zipped together
	        first_zip = list(zip(slice_to_zip, word2))
	        # Append the slice_to_append to the end of the list
	        first_zip.append(slice_to_append)
	        # Join all the variables into a list using list comprehension
	        first_join = [''.join(s) for s in first_zip]
	        # Finally join everything one final time to get the merged string
	        return(''.join(first_join))
