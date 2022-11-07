# This problem is called 326. Power of Three
# You can access it here: https://leetcode.com/problems/power-of-three/

# The program will be given an integer n
# and the program will return true if it is a power of three. 
# Otherwise, it will return false.
# An integer n is a power of three, if there exists an integer x such that n == 3^x.
# For example if n = 27 
# The program will return true
# Because 3^3 = 27

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False 
        while (n%3==0):
            temp = n/3
            n = n/3 
        return n == 1