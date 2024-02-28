# Kids With the Greatest Number of Candies

# There are n kids with candies. You are given an integer array candies,
#  where each candies[i] represents the number of candies the ith kid has,
#   and an integer extraCandies, denoting the number of extra candies that you have.

# Return a boolean array result of length n, where result[i] is true if,
#  after giving the ith kid all the extraCandies,
#   they will have the greatest number of candies among all the kids, or false otherwise.

# Note that multiple kids can have the greatest number of candies.


# Example 1:

# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true] 
# Explanation: If you give all extraCandies to:
# - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
# - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
# - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
# - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
# - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

# Example 2:

# Input: candies = [4,2,1,1,2], extraCandies = 1
# Output: [true,false,false,false,false] 
# Explanation: There is only 1 extra candy.
# Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.
# Example 3:

# Input: candies = [12,1,12], extraCandies = 10
# Output: [true,false,true]
 

# Constraints:

# n == candies.length
# 2 <= n <= 100
# 1 <= candies[i] <= 100
# 1 <= extraCandies <= 50

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# February 28th, 2024
# First Attempt
# A simple brute force solution that has a decently fast runtime and decent memory efficiency
# All test cases passed
# Runtime: 41ms (Beats 57.42% of users with Python3)
# Memory: 16.52 MB (Beats 66.34% of users with Python3)

# class Solution:
#     def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
#         maxCandies = max(candies)
#         result = []

#         for candy in candies:
#         	if candy + extraCandies >= maxCandies:
#         		result.append(True)
#         	else:
#         		result.append(False)

#         return result


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# February 28th, 2024
# Second Attempt
# I wanted to try a solution using list comprehension instead of a for loop to see if it was more effecient
# To my surprise, this solution has a much faster runtime while using the same amount of memory
# All test cases passed
# Runtime: 32ms (Beats 94.86% of users with Python3)
# Memory: 16.52 MB (Beats 66.34% of users with Python3)

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxCandies = max(candies)
        result = [c + extraCandies >= maxCandies for c in candies]

        return result


sol = Solution()

print(sol.kidsWithCandies([12,1,12], 10))