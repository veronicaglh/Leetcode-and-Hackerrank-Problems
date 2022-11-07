# This problem is called 342. Power of Four
# You can access it here: https://leetcode.com/problems/power-of-four/

# The program will be given an integer n
# and the program will return true if it is a power of four. 
# Otherwise, it will return false.
# An integer n is a power of four, if there exists an integer x such that n == 4^x.
# For example if n = 16
# The program will return true
# Because 4^2 = 16

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False 
        while (n%4==0):
            temp = n/4
            n = n/4 
        return n == 1