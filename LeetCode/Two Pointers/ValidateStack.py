# This problem is called 946. Validate Stack Sequences
# You can access it here: https://leetcode.com/problems/validate-stack-sequences/

# The program recieves  two integer arrays pushed and popped each with distinct values
# It will then return true if this could have been the result of a sequence of push and 
# pop operations on an initially empty stack, or false otherwise.
# For example if  pushed = [1,2,3,4,5] and popped = [4,5,3,2,1]
# The output: true
# Because: 
# -  We can do the following sequence:
# - push(1), push(2), push(3), push(4),
# - pop() -> 4,
# - push(5),
# - pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        index = 0 

        for p in pushed: 
            stack.append(p)
            while stack and index<len(popped) and stack[-1]==popped[index]:
                index += 1 
                stack.pop()
                
        return stack ==[]
