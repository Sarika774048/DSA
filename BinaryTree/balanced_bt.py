LeetCode 110 - Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            lh = height(root.left)
            rh = height(root.right)

            if lh == -1 or rh == -1 or abs(rh - lh) > 1:
                return -1
            return max(lh, rh) + 1
            
        return height(root) != -1
    
        
