# Contains Duplicate 

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# October 18th, 2023
# First Attempt

# This solution is not very optimized (it's slow lol) and there are faster ways to do this with hashmaps but I haven't learned those yet
# I also completed forgot that sets exist during my first attempt lol, second attempt uses sets
# 75/75 test cases passed.
# Runtime: 527 ms (Your runtime beats 5.03 % of python3 submissions.)
# Memory Usage: 28.5 MB (Your memory usage beats  93.54 % of python3 submissions.)

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
    	# first I sorted the list so that if there are any duplicates they're right beside one another and stored it in the variable sort
        sort = sorted(nums)
        # initialized a counter for the index of the sort list
        i = 0
        # initialized the result, default value is False
        result = False
        # looping through the sort list
        for s in sort:
        	# checking to see if i is less than the length of the list minus one to prevent list index out of range error
        	if i < len(sort) - 1:
        		# if the value of sort[i] is equal to the value of sort[i+1], it means there are duplicate values 
        		if sort[i] == sort[i+1]:
        			# because there are duplicate values, result is set to True and we break out of the for loop
        			result = True
        			break
        		# if the value of sort[i] and sort[i+1] are not equal, then we increase the i counter variable by 1 and loop through the next two values
        		else:
        			i += 1
        # once the for loop has ended or been broken out of we return the result
        return result

# Tests
sol = Solution()
print(sol.containsDuplicate([1,2,3,1])) # True
print(sol.containsDuplicate([1,2,3,4])) # False
print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2])) # True


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# October 18th, 2023
# Second Attempt

# Remembered that sets are a thing that exists which simplifies the function immensely
# This solution is faster than my inital solution but it uses more memory
# 75/75 test cases passed.
# Runtime: 499 ms (Your runtime beats 18.41 % of python3 submissions.)
# Memory Usage: 31.9 MB (Your memory usage beats 32.09 % of python3 submissions.)

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
    	# if the length of the set of nums doesn't equal the length of the nums list that means there are duplicate values
    	return len(set(nums)) != len(nums)

sol = Solution()
print(sol.containsDuplicate([1,2,3,1])) # True
print(sol.containsDuplicate([1,2,3,4])) # False
print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2])) # True





