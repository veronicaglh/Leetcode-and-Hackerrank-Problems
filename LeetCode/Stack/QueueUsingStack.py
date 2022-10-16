# This problem is called 232. Implement Queue using Stacks
# You can access it here: https://leetcode.com/problems/implement-queue-using-stacks/

# This program will implement a queue using two stacks. 
# The implemented queue will support all the functions of a normal queue (push, peek, pop, and empty).
# The push function: pushes element x to the back of the queue.
# The pop function: removes the element from the front of the queue and returns it.
# The peek function: returns the element at the front of the queue.
# The empty function: Returns true if the queue is empty, false otherwise
# For example if input is: 
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Then the Output will be:
# [null, null, null, 1, 1, false] 




class MyQueue:

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []


    def push(self, x: int) -> None:
         self.push_stack.append(x)
 
      
    def pop(self) -> int:
        if self.empty(): return
        if len(self.pop_stack)!=0:
            return self.pop_stack.pop()
        if len(self.pop_stack)==0:
            while len(self.push_stack):
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack.pop()
                       

    def peek(self) -> int:
        if self.empty(): return
        if len(self.pop_stack):
            return self.pop_stack[len(self.pop_stack)- 1]
        else:
            while len(self.push_stack):
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack[len(self.pop_stack)- 1]


    def empty(self) -> bool:
        return len(self.push_stack)==False and len(self.pop_stack) == False
        
