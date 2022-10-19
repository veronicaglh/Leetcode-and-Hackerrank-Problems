# This problem is called 82. Remove Duplicates from Sorted List II
# You can access it here: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# The program recieves  the head of a sorted linked list and then will delete all nodes that have duplicate numbers. 
# It will then return the list with distinct values. The list will also be sorted.
# For example if the input is: 
# head = [1,2,3,3,4,4,5]
# Then the output will be:
# Output: [1,2,5]
# If the input is: 
# head = [1,1,1,2,3]
# The output will be:
# [2,3]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        counter = {}
        intial = ListNode(0)
        intial.next = head
      
        while head:
            counter[head.val] = counter.get(head.val, 0) + 1            
            head = head.next
                        
        head = intial.next
        previous = intial
                
        while head:
            if counter[head.val] > 1:
                previous.next = head.next
            else:
                previous = head
            head = head.next
            
        return intial.next
        
