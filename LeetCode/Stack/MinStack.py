# This problem is called 155. Min Stack
# You can access it here: https://leetcode.com/problems/min-stack/

# This program will design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# The push function: pushes element val to the stack.
# The pop function: removes the element from the top of the stack.
# The top function: gets the top element of the stack and returns it.
# The getMin function: retrieves the minimum element in the stack.
# For example if input is: 
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# Then the output will be:
# [null,null,null,null,-3,null,0,-2]

class MinStack(object):

    def __init__(self):
        # Create two lists. 
        # The stack list will hold all the values.
        # The min_stack list will contain the minimum value
        self.stack = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
        # Appending val(which is an integer value) into stack 
        # Will only append val to min_stack if min_stack is empty 
        # or if val is less than the the value that is already in min_stack
        self.stack.append(val)
        if len(self.min_stack) ==0 or self.min_stack[len(self.min_stack) - 1] >= val:
            self.min_stack.append(val)
        
    def pop(self) -> None:
        # If the popped value(from stack) is the same as the value in min_stack
        # Program will also pop that value from min_stack
        popped_value = self.stack.pop()
        if popped_value == self.min_stack[len(self.min_stack) - 1]: 
            self.min_stack.pop()
            
    def top(self) -> int:
        # Will return the value in stack as long as list is not empty
        if len(self.stack)!= 0: 
            return self.stack[-1]
        
    def getMin(self) -> int:
        # Will return the minimum value as long as min_stack is not empty
        if len(self.min_stack)!=0:
            return self.min_stack[-1]