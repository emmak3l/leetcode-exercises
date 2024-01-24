# Fizz Buzz

# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

# Example 1:

# Input: n = 3
# Output: ["1","2","Fizz"]
# Example 2:

# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
# Example 3:

# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
 

# Constraints:

# 1 <= n <= 104

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# January 24th, 2024
# First Attempt
# This was a very straightforward solution that has a fast runtime and fairly good memory usage
# 8 / 8 test cases passed.
# Runtime: 38 ms (Your runtime beats 91.57 % of python3 submissions.)
# Memory Usage: 17.7 MB (Your memory usage beats 53.68 % of python3 submissions.)

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
    	output = list(range(1,n+1))

    	for val in output:
    		if val % 3 == 0 and val % 5 == 0:
    			output[val-1] = "FizzBuzz"
    		elif val % 3 == 0:
    			output[val-1] = "Fizz"
    		elif val % 5 == 0:
    			output[val-1] = "Buzz"
    		else:
    			output[val-1] = str(val)

    	return output

sol = Solution()

print(sol.fizzBuzz(15))