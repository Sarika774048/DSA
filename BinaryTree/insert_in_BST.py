LeetCode 701 - Insert into Binary Search Tree

ou are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

Example 1:

Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: 
            return TreeNode(val)
        new_node = TreeNode(val)
        cur = root
        while root:
            if cur.val > val:
                if cur.left:
                    cur  = cur.left
                else: 
                    cur.left = new_node
                    break
                
            else:
                if cur.right: 
                    cur  = cur.right
                else: 
                    cur.right = new_node  
                    break
               
        return root

        
