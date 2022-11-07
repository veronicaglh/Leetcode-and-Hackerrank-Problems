# This problem is called 509. Fibonacci Number
# You can access it here: https://leetcode.com/problems/fibonacci-number/

# The program recieves an integer value n
# and will return the fibonacci sequence of that number n, 
# The Fibonacci numbers, commonly denoted F(n) form a sequence,
#  called the Fibonacci sequence, such that each number is the
#  sum of the two preceding ones, starting from 0 and 1. That is 
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# For example if n = 2
# The program returns 1
# Because F(2) = F(1) + F(0) = 1 + 0 = 1.

class Solution:
    def fib(self, n: int) -> int:
        value_dict= {0:0,1:1}
        for i in range(2,n+1):
            value_dict[i] = value_dict[i-1] + value_dict[i-2]
        return(value_dict[n])
        
        