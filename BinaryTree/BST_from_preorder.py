LeetCode 1008 - Construct Binary Search Tree from Preorder traversal

Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.
      
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def helper(A, i, bound):
            if i == len(A) or A[i] > bound:
                return None, i
            root = TreeNode(A[i])
            i+=1
            root.left, i = helper(A, i, root.val)
            root.right, i = helper(A, i, bound)
            return root, i
        root, _ = helper(preorder, 0, float('inf'))
        return root

        

        
        



                                           
