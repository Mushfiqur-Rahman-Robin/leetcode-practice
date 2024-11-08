# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()  
            n += 1

            if n == k:
                return curr.val

            curr = curr.right  
        

# Time Complexity: O(n) (for traversing up to k nodes)
# Space Complexity: O(n) (worst case, unbalanced tree), O(logn) (average case, balanced tree)
# Tutorial Link: https://www.youtube.com/watch?v=5LUXSvjmGCw
