# Container With Most Water

# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, 
# such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


# Example 1:

				 #   |_________|____
				 #   |         |   |
				 #   | |       |   |
				 #   | |   |   |   |
				 #   | |   | | |   |
				 #   | |   | | | | |
				 #   | | | | | | | |
                 # | | | | | | | | |
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:

# Input: height = [1,1]
# Output: 1

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# March 22nd, 2024
# First Attempt
# This solution doesn't work but I wanted to save my progress for future reference, i think i was almost there
# There are lots of prints in between because I was troubleshooting

# class Solution:
#     def maxArea(self, height: list[int]) -> int:
#     	if len(height) == 2:
#     		return min(height)

#     	maxContainer = 0
#     	tempContainer = 0
#     	i = 0
#     	j = len(height) - 1

#     	while j > i:
#     		if height[i] < 1:
#     			print("first")
#     			i += 1
#     		if height[j] < 1:
#     			print("second")
#     			j -= 1
#     		if height[i] > height[j] or height[i] < height[j]:
#     			print("third")
#     			print(tempContainer, maxContainer)
#     			tempContainer = min(height[i], height[j]) * (j - i)
#     			maxContainer = max(tempContainer, maxContainer)
#     			print(tempContainer, maxContainer)

#     			if height[i] > height[j]:
#     				print("third.1")
#     				print("i: ",height[i],"j: ", height[j])
#     				j -= 1
#     				print("i: ",height[i],"j: ", height[j])

#     			elif height[i] < height[j]:
#     				print("third.2")
#     				print("i: ",height[i],"j: ", height[j])
#     				if height[i + 1] == 0:
#     					while height[i+1] == 0:
#     						i += 1
#     				i += 1
#     				print("i: ",height[i],"j: ", height[j])
#     		else:
#     			print("fourth")
#     			print(tempContainer, maxContainer)
#     			tempContainer = min(height[i], height[j]) * j
#     			maxContainer = max(tempContainer, maxContainer)
#     			print(tempContainer, maxContainer)
#     			print("i: ",height[i],"j: ", height[j])
#     			j -= 1
#     			print("i: ",height[i],"j: ", height[j])
    		
#     	return maxContainer

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# March 22nd, 2024
# NeetCode Solution
# I couldn't solve this in a reasonable time so I looked up NeetCode's solution so I know how to do it in the future
# My solution was soooo close to this one!!! I just got a little mixed up
# Runtime: 524ms (Beats 60.09% of users with Python3)
# Memory: 29.30 MB (Beats 84.61% of users with Python3)


class Solution:
    def maxArea(self, height: list[int]) -> int:
    	maxContainer = 0
    	i = 0
    	j = len(height) - 1

    	while i < j:
    		tempContainer = min(height[i], height[j]) * (j - i)
    		maxContainer = max(maxContainer, tempContainer)
    		if height[i] < height[j]:
    			i += 1
    		elif height[i] > height[j]:
    			j -= 1
    		else:
    			j -= 1

    	return maxContainer

sol = Solution()

print(sol.maxArea([1,0,0,0,0,0,0,2,2]))