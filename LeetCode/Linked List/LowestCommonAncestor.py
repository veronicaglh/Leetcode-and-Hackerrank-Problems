# This problem is called 236. Lowest Common Ancestor of a Binary Tree
# You can access it here: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# The program will be given a binary tree
# It will return the lowest common ancestor (LCA) of two given nodes in the tree
# “The lowest common ancestor is defined between two nodes p and q as the lowest node 
# in T that has both p and q as descendants (where we allow a node to be a descendant 
# of itself).”
# For example if root = [3,5,1,6,2,0,8,null,null,7,4] and  p = 5 and q = 1
# The output will be 3
# Because: The LCA of nodes 5 and 1 is 3.
# If root = [3,5,1,6,2,0,8,null,null,7,4] and p = 5 and q = 4
# The output will be 5
# Because: The LCA of nodes 5 and 4 is 5, since a node can be 
# a descendant of itself according to the LCA definition.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left or right
