# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]

        def backtrack(node, max_val):
            if not node:
                return 0
            
            if node.val >= max_val:
                res[0] += 1
            
            new_max = max(node.val, max_val)
            
            backtrack(node.left, new_max)
            backtrack(node.right, new_max)
    
        backtrack(root, root.val)
        return res[0]
        

# time complexity: O(n)
# space complexity: In the worst case, h = O(n) for a skewed tree, and in the best case, h = O(log n) for a balanced tree.
# check note
        
