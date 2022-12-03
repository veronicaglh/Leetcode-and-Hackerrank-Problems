# This problem is called 237. Delete Node in a Linked List
# You can access it here: https://leetcode.com/problems/delete-node-in-a-linked-list/

# The program recieves a singly-linked list head and it will delete a node(node) in it.
# The program is given the node to be deleted(node)
# After the node has been deleted then: 
# - The value of the given node should not exist in the linked list.
# - The number of nodes in the linked list should decrease by one.
# - All the values before node should be in the same order.
# - All the values after node should be in the same order.
# Custom testing:
# - For the input, the program will provide the entire linked list head and the node to 
#   be given node. node should not be the last node of the list and should be an actual node in the list.
# - The linked list will be built and pass the node to the function.
# - The program will return the entire list after calling the function.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next    