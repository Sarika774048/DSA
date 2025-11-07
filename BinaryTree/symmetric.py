LeetCode 101 - Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def traverse(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return ( t1.val == t2.val and traverse(t1.left, t2.right) and traverse(t1.right, t2.left))
        
        return traverse(root.left, root.right)
       
            
            
