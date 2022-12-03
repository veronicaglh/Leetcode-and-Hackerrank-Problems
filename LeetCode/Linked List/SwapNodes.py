# This problem is called 24. Swap Nodes in Pairs
# You can access it here: https://leetcode.com/problems/swap-nodes-in-pairs/

# The program will be given  a linked list(head)
# It will then swap every two adjacent nodes and return its head.
# For example: 
# If head = [1,2,3,4]
# Then the output is [2,1,4,3]
# If head = [1]
# Then the output = [1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        initial = ListNode(0)
        initial.next = head
        current = initial

        while current.next is not None and current.next.next is not None:
            first = current.next
            second = current.next.next

            first.next = second.next
            current.next = second

            current.next.next = first
            current = current.next.next

        return initial.next