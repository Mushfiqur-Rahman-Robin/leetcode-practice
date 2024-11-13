# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            maxLeft = dfs(root.left)
            maxRight = dfs(root.right)
            maxLeft = max(maxLeft, 0)
            maxRight = max(maxRight, 0)

            res[0] = max(res[0], maxLeft + root.val + maxRight)

            return root.val + max(maxLeft, maxRight)
        
        dfs(root)
        return res[0]
            

# Tutorial link: https://www.youtube.com/watch?v=Hr5cWUld4vU
# Time Complexity: O(N), where N is the total number of nodes in the tree.
# Space Complexity (for the call stack in a balanced tree): O(H), where H is the height of the tree (in the worst case, H=N for a skewed tree, making the space complexity O(N)).
