LeetCode 230 - Kth Smallest Element in BST

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.result = None

        def inorder(root):
            if not root or self.result is not None:
                return 
            inorder(root.left)
            self.count +=1
            if self.count == k:
                self.result = root.val
                return 
            inorder(root.right)
        inorder(root)
        return self.result
            
        
        

        
