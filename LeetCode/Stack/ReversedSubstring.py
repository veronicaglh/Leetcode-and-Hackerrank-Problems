# This problem is called 1190. Reverse Substrings Between Each Pair of Parentheses
# You can access it here: https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

# This program will recieve a string (named s) that consists of lower case English letters and brackets.
# The program will then reverse the strings in each pair of matching parentheses, starting from the innermost one.
# The final result will not contain any brackets.
# For example if the string s is: 
# s = "(abcd)"
# The the output will be:
# Output: "dcba"
# If the string s is:
# s = "(u(love)i)"
# Then the output will be:
# Output: "iloveu"

class Solution:
    def reverseParentheses(self, s: str) -> str:
        # Create two lists 
        # The first list(stack) will store the characters of s 
        # Second list(reversed_stack) will store the reversed characters
        stack = []
        reversed_stack = []

        for char in s:
            # Will append characters of s into the stack until character is equivalent to closing bracket.
            if char != ')': 
                stack.append(char)

            # If character is equivalent to closing bracket then the program pops values from stack. 
            # If the value that has been popped from stack is equivalent to a opening bracket 
            # then the characters are appended into reversed_stack in reverse order.
            else:
                for i in range(len(stack)):
                    popped_value = stack.pop()
                    if popped_value!='(':
                        reversed_stack.append(popped_value)
                    else: 
                        break
                    
                    
                for i in reversed_stack: 
                    stack.append(i)
                reversed_stack = []
        return ''.join(stack)