# Remove Element

# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. 
# Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, 
# you need to do the following things:


# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
# The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int val = ...; // Value to remove
# int[] expectedNums = [...]; // The expected answer with correct length.
#                             // It is sorted with no values equaling val.

# int k = removeElement(nums, val); // Calls your implementation

# assert k == expectedNums.length;
# sort(nums, 0, k); // Sort the first k elements of nums
# for (int i = 0; i < actualLength; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

 

# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: 
# Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: 
# Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).
 

# Constraints:

# 0 <= nums.length <= 100
# 0 <= nums[i] <= 50
# 0 <= val <= 100

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# February 8th, 2024
# First Attempt
# I tried to solve this on my own with a two pointer solution but it did not work for all the test cases
# I spent an hour trying to solve it on my own but couldn't so I looked up the solution

# class Solution:
#     def removeElement(self, nums: list[int], val: int) -> int:
#     	i = 0
#     	j = len(nums) - 1
#     	k = 0

#     	while i <= j:
#     		if nums[i] != val:
#     			k += 1
#     		if nums[j] == val:
#     			nums.remove(nums[j])
#     			j -= 1
#     		if nums[i] == val:
#     			nums[i], nums[j] = nums[j], nums[i]
#     			nums.remove(nums[j])
#     			j -= 1
    		
#     		i += 1

#     	if len(nums) == 1:
#     		if nums[0] == val:
#     			nums.remove(val)
#     			return k
#     		else:
#     			return k + 1

#     	if nums == []:
#     		return k

#     	return k + 1, nums

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# February 8th, 2024
# Second Attempt (NeetCode Solution)
# This was the most straightforward example solution I found and after watching the video I understand where
# I went wrong with my initial solution, which is good. A learning opportunity!
# This solution has a decently fast runtime and excellent memory usage
# All test cases passed
# Runtime: 39ms (Beats 55.46% of users with Python3)
# Memory: 16.47 MB (Beats 82.40% of users with Python3)

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
        	if nums[i] != val:
        		nums[k] = nums[i]
        		k += 1

        return k


sol = Solution()

nums = [3,2,2,3]
val = 3
print(sol.removeElement(nums, val))
















