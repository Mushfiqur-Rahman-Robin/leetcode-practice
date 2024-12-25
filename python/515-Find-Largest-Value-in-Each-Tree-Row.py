# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        max_in_each_row = []
        tmp_res = []

        def level_order_bfs(root):
            if not root:
                return []

            queue = deque([root])

            while queue:
                # level = []
                level_max = float("-inf")

                for i in range(len(queue)): 
                    node = queue.popleft()
                    # level.append(node.val)
                    level_max = max(level_max, node.val)
                
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                
                max_in_each_row.append(level_max)

            #     tmp_res.append(level)
            
            # for lsts in tmp_res:
            #     max_in_each_row.append(max(lsts))
            
            
            return max_in_each_row

        level_order_bfs(root)
        return max_in_each_row
        

# this problem extends Leetcode 102. Binary Tree Level Order Traversal
# time complexity: O(n)
# space complexity: O(n)
