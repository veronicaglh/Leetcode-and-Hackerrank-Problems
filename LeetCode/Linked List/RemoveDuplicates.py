# This problem is called 83. Remove Duplicates from Sorted List
# You can access it here: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# The program will be given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
# Return the linked list sorted as well.
# For example if head = [1,1,2]
# The output will be [1, 2]
# For example if head = [1,1,2,3,3]
# The output will be [1,2,3]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        list = head
        
        while(list.next!=None):
            if list.val == list.next.val:
                list.next = list.next.next
            else:
                list = list.next
        
        return head