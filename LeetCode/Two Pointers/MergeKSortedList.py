# This problem is called 23. Merge k Sorted Lists
# You can access it here: https://leetcode.com/problems/merge-k-sorted-lists/

# The program will be given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# The program will Merge all the linked-lists into one sorted linked-list and return it.
# For example if lists = [[1,4,5],[1,3,4],[2,6]]
# Then the output will be [1,1,2,3,4,4,5,6]
# Because: 
# - The linked-lists are:
# [ 1->4->5, 1->3->4, 2->6 ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        root = result = ListNode(None)

        for l in lists:
            while l:
                heappush(heap, l.val)
                l = l.next

        while heap:
            result.next = ListNode(heappop(heap))
            result = result.next
        return root.next