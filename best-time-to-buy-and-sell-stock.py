# Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock 
# and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# February 12th, 2024
# First Attempt
# Used a two pointer approach to solve this problem
# Both the runtime and memory usage are fairly decent compared to other python3 submissions
# All test cases passed
# Runtime: 761ms (Beats 60.28% of users with Python3)
# Memory: 16.74 MB (Beats 66.85% of users with Python3)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        i = 0
        j = 1
        maxProfit = 0

        while j < len(prices):
        	if prices[i] < prices[j]:
        		profit = prices[j] - prices[i]
        		maxProfit = max(maxProfit, profit)
        	else:
        		i = j

        	j += 1

        return maxProfit

sol = Solution()

print(sol.maxProfit([7,1,5,3,6,4]))