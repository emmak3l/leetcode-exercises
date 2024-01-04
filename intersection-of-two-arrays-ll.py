# Intersection of Two Arrays II

# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.


# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
 

# Follow up:

# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# January 4th, 2024
# First Attempt
# Complete brute force first attempt, it works but is very slow and uses a lot of memory
# I was trying a bunch of different methods before I found one that worked, that's why there's both list comprehension and regular for loops
# I have drastically simplified this code in my second attempt
# 57 / 57 test cases passed.
# Runtime: 84 ms (Your runtime beats 10.52 % of python3 submissions.)
# Memory Usage: 17.5 MB

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
    	result1 = [x for x in nums1 if x in nums2]
    	result2 = [x for x in nums2 if x in nums1]
    	result3 = []

    	if len(result1) < len(result2):
    		for x in result1:
    			if x in nums1 and x in nums2:
    				result3.append(x)
    				nums1.remove(x)
    				nums2.remove(x)
    		return result3
    	else:
    		for x in result2:
    			if x in nums1 and x in nums2:
    				result3.append(x)
    				nums1.remove(x)
    				nums2.remove(x)
    		return result3


s = Solution()

# nums1 = [61,24,20,58,95,53,17,32,45,85,70,20,83,62,35,89,5,95,12,86,58,77,30,64,46,13,5,92,67,40,20,38,31,18,89,85,7,30,67,34,62,35,47,98,3,41,53,26,66,40,54,44,57,46,70,60,4,63,82,42,65,59,17,98,29,72,1,96,82,66,98,6,92,31,43,81,88,60,10,55,66,82,0,79,11,81]
# nums2 = [5,25,4,39,57,49,93,79,7,8,49,89,2,7,73,88,45,15,34,92,84,38,85,34,16,6,99,0,2,36,68,52,73,50,77,44,61,48]

nums1 = [1,2,2,1]
nums2 = [2,2]

print(s.intersect(nums1, nums2))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# January 4th, 2024
# Second Attempt
# I realized that I could drastically simplify my previous attempt and make it DRY in the process
# This code is faster than my first attempt (still not ideal) and it still uses a lot of memory

# 57 / 57 test cases passed.
# Runtime: 57 ms (Your runtime beats 42.89 % of python3 submissions.)
# Memory Usage: 17.6 MB

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        for num in nums1:
            if num in nums2:
                result.append(num)
                nums2.remove(num)
        return result