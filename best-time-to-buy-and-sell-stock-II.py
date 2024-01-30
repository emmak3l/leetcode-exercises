# Best Time to Buy and Sell Stock II


# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock.
# You can only hold at most one share of the stock at any time. 
# However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.
# Example 2:

# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.
# Example 3:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 

# Constraints:

# 1 <= prices.length <= 3 * 104
# 0 <= prices[i] <= 104

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# January 30th, 2024
# First Attempt
# This problem was very straightforward to solve, if the stock is worth more than the previous day you sell and record the profit
# The runtime is very fast and the memory usage is also very decent compared to other submitted solutions
# 200 / 200 test cases passed.
# Runtime: 51 ms (Your runtime beats 94.50 % of python3 submissions.)
# Memory Usage: 18 MB (Your memory usage beats 58.87 % of python3 submissions.)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0

        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit


sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))


