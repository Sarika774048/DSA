LeetCode 222 - Count Complete Tree Nodes

Given the root of a complete binary tree, return the number of the nodes in the tree.
According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
Design an algorithm that runs in less than O(n) time complexity.

Example 1:

Input: root = [1,2,3,4,5,6]
Output: 6

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.count = 0

        def pre(root):
            if not root:
                return
            self.count +=1
            pre(root.left)
            pre(root.right)
            return self.count
        pre(root)
        return self.count
        
            
        
