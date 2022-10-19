# This problem is called 876. Middle of the Linked List
# You can access it here: https://leetcode.com/problems/middle-of-the-linked-list/


# The program recieves the head of a singly linked list
# and returns the middle node of the linked list.
# If there are two middle nodes, the program will return the second middle node.
# For example if head =  [1,2,3,4,5] 
# Then the  output will be [3,4,5] 
# The middle node of the list is 3.
# If head = [1,2,3,4,5,6]
# Then the output will be [4,5,6]
# The list has two middle nodes: 3 and 4 
# The program will return the second middle node.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Set both fast and slow to the value of head. So they begin at the same entry. 
        fast = head
        slow = head
        # Create while loop so that fast can go two times as fast as slow. 
        # For example if list = [1,2,3,4,5]
        # When slow = 3 then fast = 5. 
        # Meaning the value of slow will always be the middle node.
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

            
        
