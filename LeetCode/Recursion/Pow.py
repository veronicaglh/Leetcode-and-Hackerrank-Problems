# This problem is called 50. Pow(x, n)
# You can access it here: https://leetcode.com/problems/powx-n/

# The program is  given a number x as well as n. 
# It will return x^n
# For example if x = 2.00000 and n = 10
# The output will be 1024.00000

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return(pow(x,n))