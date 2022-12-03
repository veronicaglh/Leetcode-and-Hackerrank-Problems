# This problem is called 1019. Next Greater Node In Linked List
# You can access it here: https://leetcode.com/problems/next-greater-node-in-linked-list/

# The program will be given the head of a linked list with n nodes.
# For each node in the list, it will find the value of the next greater node.
# That is, for each node, find the value of the first node that is next to it 
# and has a strictly larger value than it.
# The program will return an integer array answer where answer[i] is the value 
# of the next greater node of the ith node (1-indexed). If the ith node does 
# not have a next greater node, set answer[i] = 0.
# For example: 
# If head = [2,1,5]
# Then the output is [5,5,0]
# If head = [2,7,4,3,5]
# Then the output is [7,0,5,5,0]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        node_values = []
        current = head 

        while current:
            node_values.append(current.val)
            current = current.next 
        answer = [0] * len(node_values)
        stack = []

        for index, value in enumerate(node_values):
            while stack and node_values[stack[-1]] < value:
                answer[stack.pop()] = value
            stack.append(index)

        return answer