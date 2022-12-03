# This problem is called 206. Reverse Linked List
# You can access it here: https://leetcode.com/problems/reverse-nodes-in-k-group/

# The program will be given the head of a linked list, reverse the nodes of the 
# list k at a time, and return the modified list.
# k is a positive integer and is less than or equal to the length of the linked 
# list. If the number of nodes is not a multiple of k then left-out nodes, in 
# the end, should remain as it is.
# For example: 
# If head = [1,2,3,4,5] and k = 2
# Then the output is [2,1,4,3,5]
# If head =  [1,2,3,4,5] and k = 3
# Then the output is [3,2,1,4,5]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head is None or k < 2:
            return head

        temp = ListNode(0)
        temp.next = head
        start = temp
        end = head
        count = 0

        while end:
            count += 1
            if count % k == 0:
                start = self.reverse(start, end.next)
                end = start.next
            else:
                end = end.next
        return temp.next
    
    def reverse(self, start, end):
        previous = start
        current = start.next
        first = current

        while current != end:
            temp2 = current.next
            current.next = previous
            previous = current
            current = temp2
        start.next = previous
        first.next = current
        
        return first

