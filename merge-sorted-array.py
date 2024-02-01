# Merge Sorted Array

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that 
# should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. 
# The 0 is only there to ensure the merge result can fit in nums1.
 

# Constraints:

# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109
 

# Follow up: Can you come up with an algorithm that runs in O(m + n) time?

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# February 1st, 2024
# First Attempt
# I had just learned how to do merge as part of mergeSort in my javascript data structures and algorithms udemy course
# I tweaked the implementation to work with python and the final solution is incredibly fast and very memory efficent
# 59 / 59 test cases passed.
# Runtime: 30 ms (Your runtime beats 98.14 % of python3 submissions.)
# Memory Usage: 16.5 MB (Your memory usage beats 69.21 % of python3 submissions.)

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        result = []

        while i < m and j < n:
        	if nums1[i] < nums2[j]:
        		result.append(nums1[i])
        		i += 1
        	else:
        		result.append(nums2[j])
        		j += 1
        while i < m:
        	result.append(nums1[i])
        	i += 1
        while j < n:
        	result.append(nums2[j])
        	j += 1
        nums1.clear()
        nums1.extend(result)

sol = Solution()

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

print(f"Before merge: {nums1}")
sol.merge(nums1,m,nums2,n)
print(f"After merge: {nums1}")