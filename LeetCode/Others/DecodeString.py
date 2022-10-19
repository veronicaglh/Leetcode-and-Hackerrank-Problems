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