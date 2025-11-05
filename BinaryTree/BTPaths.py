LeetCode 257 - Binary Tree Paths

Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.

Example 1:

Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path, result):
            if not node: 
                return 
            path.append(str(node.val))

            if not node.left and not node.right:
                result.append("->".join(path))
            else:
                dfs(node.left, path, result)
                dfs(node.right, path, result)
            path.pop()
        result = []
        dfs(root, [], result)
        return result
        


        
