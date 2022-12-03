# This problem is called 234. Palindrome Linked List
# You can access it here: https://leetcode.com/problems/palindrome-linked-list/

# The program will be given the head of a singly linked list.
# It will then return true if it is a palindrome or false otherwise.
# For example: 
# If head = head = [1,2,2,1]
# Then the output is true
# If head = [1,2]
# Then the output = false

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        node = None

        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
            
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next

        return True