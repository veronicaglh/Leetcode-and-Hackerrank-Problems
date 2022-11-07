# This problem is called 1969. Minimum Non-Zero Product of the Array Elements
# You can access it here: https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/

# The program is  given a positive integer p. Consider an array nums (1-indexed) that consists of the integers in the inclusive range [1, 2p - 1] 
# in their binary representations. You are allowed to do the following operation any number of times:
# Choose two elements x and y from nums.
# Choose a bit in x and swap it with its corresponding bit in y. Corresponding bit refers to the bit that is in the same position in the other integer.
# The program will find the minimum non-zero product of nums after performing the above operation any number of times. Return this product modulo 109 + 7.
# For example if p = 16
# The program will have an output of 1 
# Because nums = [1]. There is only one element, so the product equals that element.

class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        CONST_MOD  = 10 ** 9 + 7
        top_value = pow(2,p,CONST_MOD) - 1
        mid_value = top_value - 1
        midcount = pow(2,p-1)-1
        return (pow(mid_value,midcount,CONST_MOD)*top_value)%CONST_MOD
