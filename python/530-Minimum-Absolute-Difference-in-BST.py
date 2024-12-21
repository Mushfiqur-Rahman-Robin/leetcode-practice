# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = [float('inf')]
        prev = [None]
        
        def dfs(root):
            if not root:
                return 0
            
            dfs(root.left)

            if prev[0] is not None:
                res[0] = min(res[0], abs(root.val - prev[0]))
            
            prev[0] = root.val

            dfs(root.right)
        
        dfs(root)
        return res[0]
            
# In a BST, the in-order traversal visits the left subtree, then the current node, and then the right subtree, resulting in a sorted sequence of node values.  

# time complexity: O(n)
# space complexity: O(height of the tree)
# check note
        
