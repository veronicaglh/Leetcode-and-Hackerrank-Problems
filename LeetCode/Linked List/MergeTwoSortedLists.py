# This problem is called 21. Merge Two Sorted Lists
# You can access it here: https://leetcode.com/problems/merge-two-sorted-lists/

# The program will be given given the heads of two sorted linked lists list1 and list2.
# It will merge the two lists in a one sorted list
# The list should be made by splicing together the nodes of the first two lists.
# The program will return the head of the merged linked list.
# For example if list1 = [1,2,4] and list2 = [1,3,4]
# The output will be [1,1,2,3,4,4]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1
        
        if list1.val < list2.val:
            temp = head = ListNode(list1.val)
            list1 = list1.next
        else:
            temp = head = ListNode(list2.val)
            list2 = list2.next
        
        while (list1 is not None or list2 is not None):
            if (list1 is None and list2 is not None):
                temp.next = ListNode(list2.val)
                list2 = list2.next
            
            elif (list1 is not None and list2 is None):
                temp.next = ListNode(list1.val)
                list1 = list1.next
            
            else:
                if(list1.val > list2.val):
                    temp.next = ListNode(list2.val)
                    list2 = list2.next
                else:
                    temp.next = ListNode(list1.val)
                    list1 = list1.next
            
            temp = temp.next
        
        return head