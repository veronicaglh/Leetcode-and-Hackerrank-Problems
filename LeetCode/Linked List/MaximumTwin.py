# This problem is called 2130. Maximum Twin Sum of a Linked List
# You can access it here: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# The program will be given the head of a linked list with even length
# It will return the maximum twin sum of the linked list.
# In a linked list of size n, where n is even, the ith node (0-indexed) 
# of the linked list is known as the twin of the (n-1-i)th node, 
# if 0 <= i <= (n / 2) - 1.
# - For example, if n = 4, then node 0 is the twin of node 3, 
# - and node 1 is the twin of node 2. These are the only nodes 
# - with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.
# - For example if head = [5,4,2,1]
# - Then the output is 6 
# Because: 
# - Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
# - There are no other nodes with twins in the linked list.
# - Thus, the maximum twin sum of the linked list is 6. 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
  def pairSum(self, head: Optional[ListNode]) -> int:
    previous = None 
    slow = fast = head 

    while fast and fast.next:
        previous = slow 
        slow = slow.next 
        fast = fast.next.next 

    previous.next = None 

    previous = None 
    current = slow 
    while current:
        next_current = current.next
        current.next = previous
        previous = current
        current = next_current

    final_result = 0 
    current1 = head 
    current2 = previous 

    while current1:
        final_result = max(final_result, current1.val + current2.val)
        current1, current2 = current1.next, current2.next

    return final_result
        

