# This problem is called 147. Insertion Sort List
# You can access it here: https://leetcode.com/problems/insertion-sort-list/

# The program will be given the head of a singly linked list
# sort the list using insertion sort algorithm
# The program will return the head of the sorted list. 
# For example if head = [4,2,1,3]
# The output will be [1,2,3,4]
# For example if head = [[-1,5,3,4,0]
# The output will be [-1,0,3,4,5]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        previous= head
        current = head.next 

        while current != 0: 
            if current.val >= previous.val: 
                previous = current
                current = current.next 
                continue 

            temp = dummy 
            while current.val > temp.next.val:
                temp = temp.next 
            previous.next = current.next 
            current.next = temp.next 
            temp.next = current
            current = previous.next

        return dummy.next