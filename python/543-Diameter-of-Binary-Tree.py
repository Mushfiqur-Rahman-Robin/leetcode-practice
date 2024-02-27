# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            nonlocal diameter

            if root is None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            diameter = max(left + right, diameter)

            return max(left, right) + 1

        diameter = 0
        dfs(root)

        return diameter
        
 # https://www.youtube.com/watch?v=bkxqA8Rfv04
 # Time complexity O(n)
