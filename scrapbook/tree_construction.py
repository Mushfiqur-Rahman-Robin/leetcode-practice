class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque

# Input list
node = [1, 4, 5, 6, None, 8, None]


# Iterative Method to Create a Tree
def create_tree_iterative(node):
    """
    Create a binary tree from a list using an iterative approach.

    Args:
    - node (List): List representation of a binary tree.

    Returns:
    - TreeNode: Root of the constructed binary tree.
    """
    if not node or node[0] is None:
        return None

    root = TreeNode(node[0])  # Initialize the root node
    queue = deque([root])  # Queue to track nodes being processed
    index = 1  # Start processing from the second element in the list

    while queue and index < len(node):
        current = queue.popleft()

        # Add left child if available
        if index < len(node) and node[index] is not None:
            current.left = TreeNode(node[index])
            queue.append(current.left)
        index += 1

        # Add right child if available
        if index < len(node) and node[index] is not None:
            current.right = TreeNode(node[index])
            queue.append(current.right)
        index += 1

    return root


# Recursive Method to Create a Tree
def create_tree_recursive(node, index=0):
    """
    Create a binary tree from a list using a recursive approach.

    Args:
    - node (List): List representation of a binary tree.
    - index (int): Current index in the list.

    Returns:
    - TreeNode: Root of the constructed binary tree.
    """
    if index >= len(node) or node[index] is None:
        return None

    root = TreeNode(node[index])  # Create the current node
    root.left = create_tree_recursive(node, 2 * index + 1)  # Left child
    root.right = create_tree_recursive(node, 2 * index + 2)  # Right child

    return root


# Function to print the tree in level order
def print_tree(root):
    """
    Prints the tree in level order.

    Args:
    - root (TreeNode): Root of the binary tree.

    Returns:
    - None
    """
    if not root:
        print("Tree is empty.")
        return

    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values for a cleaner display
    while result and result[-1] is None:
        result.pop()

    print(result)


# Iterative tree construction
root_iterative = create_tree_iterative(node)
print("Tree (Iterative):")
print_tree(root_iterative)

# Recursive tree construction
root_recursive = create_tree_recursive(node)
print("Tree (Recursive):")
print_tree(root_recursive)
