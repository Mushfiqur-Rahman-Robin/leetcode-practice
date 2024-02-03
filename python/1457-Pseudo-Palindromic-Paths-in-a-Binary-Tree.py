# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        count = defaultdict(int) # using defaultdict so that in scenario for count[i] = count[i] + X it will provide 0 if no prior value is present for count[i]

        odd = 0 # digit with odd count

        def dfs(node):
            nonlocal odd
            if not node:
                return 0

            count[node.val] += 1
            odd_change = 1 if count[node.val] % 2 == 1 else -1
            odd += odd_change

            if not node.left and not node.right:
                res = 1 if odd <= 1 else 0
            else:
                res = dfs(node.left) + dfs(node.right)
 
            odd -= odd_change
            count[node.val] -= 1

            return res

        return dfs(root)

# https://www.youtube.com/watch?v=MBsSpQnaFzg
