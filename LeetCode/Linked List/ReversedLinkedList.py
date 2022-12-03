# This problem is called 206. Reverse Linked List
# You can access it here: https://leetcode.com/problems/reverse-linked-list/

# The program will be given the head of a singly linked list
# It will then reverse the list and 
# return the list that has been reversed 
# For example: 
# If head = [1,2,3,4,5]
# Then the output is [5,4,3,2,1]
# If head = [1,2]
# Then the output = [2,1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None or head.next == None:
            return head

        next_value = head.next
        result = self.reverseList(next_value)

        head.next = None
        next_value.next = head

        return result
