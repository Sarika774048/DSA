LeetCode 450 - Delete a node in BST

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
Basically, the deletion can be divided into two stages:
Search for a node to remove.
If the node is found, delete the node.
 
Example 1:

Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findLastRight(root):
            if not root.right:
                return root
            return findLastRight(root.right)

        def helper(root):
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            rightChild = TreeNode()
            lastRight = TreeNode()
            rightChild = root.right
            lastRight = findLastRight(root.left)
            lastRight.right = rightChild
            return root.left

        

        if not root:
            return None
        if root.val == key:
            return helper(root)
        dummy = TreeNode()
        dummy = root
        while root:
            if root.val > key:
                if root.left and root.left.val == key:
                    root.left = helper(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right and root.right.val == key:
                    root.right = helper(root.right)
                    break
                else:
                    root = root.right
        return dummy

        



        
