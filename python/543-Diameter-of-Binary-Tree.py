class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], left + right)

            return 1 + max(left, right)

        dfs(root)
        return res[0]

# tutorial link: https://www.youtube.com/watch?v=K81C31ytOZE
# time complexity: O(n)
# space complexity: O(logn) for balanced tree and O(n) for unbalanced tree
# check note
