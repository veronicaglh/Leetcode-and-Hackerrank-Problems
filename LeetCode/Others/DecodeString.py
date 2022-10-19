# LeetCode is a place where programmers from all over the world come together to solve different programming problems.
# All of the questions done in this folder are from the LeetCode website. 
# In order to access and solve the problems you will need to sign up for an account on their website. 
# I have also attached a link to each problem solved so it is possible to access the problem and attempt to solve it.
# Please run the code on LeetCodes own code editor. If you try to run it on your own IDE the code will not work.
# Here is LeetCodes website: https://leetcode.com/
# Here is where you can create an account: https://leetcode.com/accounts/signup/
# This problem is called 394. Decode String
# You can access it here: https://leetcode.com/problems/decode-string/

# Given an encoded string, return its decoded string.

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curNum = 0
        curString = ''
        
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString