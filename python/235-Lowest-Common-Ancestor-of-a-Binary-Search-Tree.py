# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = [root] # Using lca = [root] effectively makes lca a mutable object (a list), so you can modify its contents within search_lca(). When you reassign lca[0] = root inside the nested function, it updates the content of the original list rather than creating a new local variable. This way, when search_lca() finishes executing, lca[0] will hold the reference to the correct ancestor node. Since lists are mutable, lca[0] = root changes the content of lca at the global level, allowing the function lowestCommonAncestor() to return the updated value of lca[0]. Thus, wrapping root in a list allows you to maintain a reference to the lowest common ancestor across the nested function.

        def search_lca(root):
            if not root:
                return
            
            lca[0] = root
            if root is p or root is q:
                return

            elif root.val < p.val and root.val < q.val:
                search_lca(root.right)

            elif root.val > p.val and root.val > q.val:
                search_lca(root.left)

            else:
                return

        
        search_lca(root)
        return lca[0]
        

# Tutorial link: https://www.youtube.com/watch?v=r6AXIfdi9oQ
# Time Complexity: O(h)
# Space Complexity: O(h) (due to the recursion stack)


# Another solution:

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         # Start at the root node and traverse down the tree
#         current = root
        
#         while current:
#             # If both `p` and `q` are greater than `current`, then LCA is in the right subtree
#             if p.val > current.val and q.val > current.val:
#                 current = current.right

#             # If both `p` and `q` are smaller than `current`, then LCA is in the left subtree
#             elif p.val < current.val and q.val < current.val:
#                 current = current.left
            
#             # If the split occurs (one of p and q is on one side, and the other is on the other),
#             # `current` is the LCA.
#             else:
#                 return current
