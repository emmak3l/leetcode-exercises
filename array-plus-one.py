# Plus One

# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.


# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
 

# Constraints:

# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain any leading 0's.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# January 3rd, 2024
# First Attempt
# This is my first brute force solution, although it's pretty fast it uses a ton of memory since I created new variables for each step
# 111 / 111 test cases passed.
# Runtime: 30 ms (Your runtime beats 96.61 % of python3 submissions.)
# Memory Usage: 17.3 MB (Your memory usage beats 13.40 % of python3 submissions.)

class Solution:
	def plusOne(self, digits: list[int]) -> list[int]:
		# Converting integer list to string list
		string_list_digits = [str(i) for i in digits]

		# Join list items using join() and convert to an int
		int_digit = int("".join(string_list_digits))

		# Increment int_digit by 1
		int_digit += 1

		# Convert str(int_digit) back to a list of ints
		int_list_digits = [int(i) for i in str(int_digit)]

		# Clear old values from digits list
		digits.clear()

		# Add new values to digits list
		digits.extend(int_list_digits)

		return digits

s = Solution()
digits = [9,9,9]

print(digits)

s.plusOne(digits)

print(digits)