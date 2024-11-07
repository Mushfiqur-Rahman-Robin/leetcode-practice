from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        queue = deque()
        queue.append(root)

        while queue:
            level = []
            n = len(queue)

            for i in range(n):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(level)
        
        return res

# Time complexity: O(n)
# Space complexity: O(n)
# Tutorial link: https://www.youtube.com/watch?v=2_tm34ZtYT4

        
        
