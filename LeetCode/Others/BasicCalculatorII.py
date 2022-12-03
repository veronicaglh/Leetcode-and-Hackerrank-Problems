# This problem is called 227. Basic Calculator II
# You can access it here: https://leetcode.com/problems/basic-calculator-ii/

# The program recieves a string s which represents a mathematical expression
# It will evaluate this expression and return its value
# For example:
# If s = "3+2*2"
# Then the output is 7 
# If s = " 3+5 / 2 "
# Then the output is 5

class Solution:
    def calculate(self, s: str) -> int: 
        def multiply(string):
            nums = string.split("*")
            ans = 1
            for n in nums:
                if "/" in n:
                    divides = n.split("/")
                    ans *= int(divides[0])
                    for i in range(1,len(divides)):
                        ans = ans//int(divides[i])
                else:
                    ans *= int(n)
            return ans
        
        s = s.replace(" ","")
        s = s.split("+")
        ans = 0
        for num in s:
            if "-" in num:
                num_reduce = num.split("-")
                temp_reduce = multiply(num_reduce[0])
                for i_r in range(1,len(num_reduce)):
                    temp_reduce -= multiply(num_reduce[i_r])
                ans += temp_reduce
            else:                
                ans += multiply(num)
        return ans                