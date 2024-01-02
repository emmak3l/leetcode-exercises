# Remove Duplicates from Sorted Array

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

 

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# January 2nd, 2024
# First Attempt
# At first I tried to convert the list to a set to eliminate all the duplicates and then convert it back to a list.
# This worked to get the correct number of unique numbers but did not work to update the list is place so I had to abandon that solution.

# Since I could not figure out a solution in the 60 minutes I gave myself, I looked up how to do it properly and came across the two pointers approach.
# I have heard about the two pointers approach before but have never implemented it myself, so although I could not solve this problem on my own I now understand how to implement a new approach to problem solving.

# 362 / 362 test cases passed.
# Runtime: 72 ms (Your runtime beats 95.72 % of python3 submissions.)
# Memory Usage: 18.6 MB (Your memory usage beats 13.59 % of python3 submissions.)

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1

s = Solution()
nums = [1,1,2]

print(s.removeDuplicates(nums))