# This problem is called 143. Reorder List
# You can access it here: https://leetcode.com/problems/reorder-list/

# The program is given the head of a singly linked-list. 
# The list can be represented as: L0 → L1 → … → Ln - 1 → Ln
# The program will then reorder the list to be on the following form::
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → ...
# It does not modify the values in the list's nodes. Only nodes themselves are modified.
# For example if the input is: head = [1,2,3,4]
# The the output will be: [1,4,2,3]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def findMid(head: ListNode):
            prev = None
            slow = head
            fast = head

            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = None

            return slow

        def reverse(head: ListNode) -> ListNode:
            prev = None
            curr = head

            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next

            return prev

        def merge(l1: ListNode, l2: ListNode) -> None:
            while l2:
                next = l1.next
                l1.next = l2
                l1 = l2
                l2 = next

        if not head or not head.next:
            return

        mid = findMid(head)
        reversed = reverse(mid)
        merge(head, reversed)