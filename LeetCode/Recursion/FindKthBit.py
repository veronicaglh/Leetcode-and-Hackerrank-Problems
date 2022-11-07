# This problem is called 1545. Find Kth Bit in Nth Binary String
# You can access it here: https://leetcode.com/problems/fibonacci-number/

# The program recieves an integer value n and k. 
# The binary string Sn is formed as follows:
# S1 = "0"
# Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
# S1 = "0", S2 = "011", S3 = "0111001", S4 = "011100110110001"
# The program will return the kth bit in Sn. It is guaranteed that k is valid for the given n
# For example if n = 3 and k = 1
# The program wil return "0"
# Because S3 is "0111001".The 1st bit is "0".

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def findk(s):
            stack = []
            for x in s: 
                if x == "0":
                    stack.append("1")
                else: 
                    stack.append("0")
            return "".join(reversed(stack))

        s = "0"
        for _ in range(n):
            s = s + "1" + findk(s)
        return s[k-1]