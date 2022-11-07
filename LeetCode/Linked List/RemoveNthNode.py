# This problem is called 19. Remove Nth Node From End of List
# You can access it here: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# The program recieves the head of a linked list 
# and will remove the nth node from the end of the list 
# and will return its head.
# For example if head = [1,2,3,4,5] and n = 2
# The output will be [1,2,3,5]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node1 = node2 = head
        len_LL = 0
        
        while head:
            len_LL += 1
            head=head.next
        head = node1
        
        if n == len_LL:
            head = head.next
            return head
        target_length = 1
        
        while target_length < (len_LL-n):
            target_length += 1
            head = head.next
            
        if head:
            head.next = head.next.next
        
        return node1
        
