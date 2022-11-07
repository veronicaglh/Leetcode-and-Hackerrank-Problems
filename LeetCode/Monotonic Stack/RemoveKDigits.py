# This problem is called 402. Remove K Digits
# You can access it here: https://leetcode.com/problems/remove-k-digits/

# The program will be given string num representing a non-negative integer num, and an integer k.
# It will then return the smallest possible integer after removing k digits from num.
# For example: if num = "1432219" and k = 3
# Then the output = "1219"
# The program will remove the three digits 4, 3, and 2
#  to form the new number 1219 which is the smallest.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num: 
            while k > 0 and len(stack) > 0 and stack[-1] > i: 
                k -= 1 
                stack.pop()
            stack.append(i)

        stack = stack[:len(stack) - k]
        result = "".join(stack)
        return str(int(result)) if result else "0"