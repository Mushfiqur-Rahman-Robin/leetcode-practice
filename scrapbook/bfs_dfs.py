from collections import deque

# Example tree representation as a list
node = [1, 4, 5, 6, None, 8, None]

# Example graph represented as an adjacency list
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}

# Tree BFS Traversal
def bfs_tree(node):
    """
    Perform BFS traversal on a binary tree represented as a list.

    Args:
    - node (List): Binary tree represented as a list.

    Returns:
    - List: BFS traversal of the tree.
    """
    if not node:  # Check for an empty tree
        return []
    
    traversal = []  # Store the BFS traversal
    queue = deque([0])  # Start BFS from the root at index 0

    while queue:
        index = queue.popleft()

        # Only process nodes that are not None
        if node[index] is not None:
            traversal.append(node[index])

        # Calculate indices for left and right children
        left = 2 * index + 1
        right = 2 * index + 2

        # Add children to the queue if they are within bounds
        if left < len(node):
            queue.append(left)
        if right < len(node):
            queue.append(right)

    return traversal


# Tree DFS Traversal (Iterative)
def dfs_tree_iterative(node):
    """
    Perform DFS traversal on a binary tree represented as a list (iterative approach).

    Args:
    - node (List): Binary tree represented as a list.

    Returns:
    - List: DFS traversal of the tree.
    """
    if not node:  # Check for an empty tree
        return []
    
    stack = [0]  # Start DFS from the root at index 0
    traversal = []  # Store the DFS traversal

    while stack:
        index = stack.pop()

        # Only process nodes that are not None
        if node[index] is not None:
            traversal.append(node[index])

            # Push right child first so that left child is processed first
            right = 2 * index + 2
            left = 2 * index + 1

            if right < len(node):
                stack.append(right)
            if left < len(node):
                stack.append(left)

    return traversal


# Tree DFS Traversal (Recursive)
def dfs_tree_recursive(node, index=0, traversal=None):
    """
    Perform DFS traversal on a binary tree represented as a list (recursive approach).

    Args:
    - node (List): Binary tree represented as a list.
    - index (int): Current index in the list representation of the tree.
    - traversal (List): List to store the DFS traversal.

    Returns:
    - List: DFS traversal of the tree.
    """
    if traversal is None:
        traversal = []

    # Stop recursion if index is out of bounds or the node is None
    if index >= len(node) or node[index] is None:
        return traversal

    traversal.append(node[index])  # Process the current node

    # Recur for left and right children
    dfs_tree_recursive(node, 2 * index + 1, traversal)  # Left child
    dfs_tree_recursive(node, 2 * index + 2, traversal)  # Right child

    return traversal


# Graph BFS Traversal
def bfs_graph(graph, start):
    """
    Perform BFS traversal on a graph represented as an adjacency list.

    Args:
    - graph (dict): Graph represented as an adjacency list.
    - start (int): Starting node for BFS.

    Returns:
    - List: BFS traversal of the graph.
    """
    visited = set()  # Keep track of visited nodes
    traversal = []  # Store the BFS traversal
    queue = deque([start])  # Start BFS from the given start node
    visited.add(start)

    while queue:
        node = queue.popleft()
        traversal.append(node)

        # Explore all neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal


# Graph DFS Traversal (Iterative)
def dfs_graph_iterative(graph, start):
    """
    Perform DFS traversal on a graph represented as an adjacency list (iterative approach).

    Args:
    - graph (dict): Graph represented as an adjacency list.
    - start (int): Starting node for DFS.

    Returns:
    - List: DFS traversal of the graph.
    """
    visited = set()  # Keep track of visited nodes
    stack = [start]  # Start DFS from the given start node
    traversal = []  # Store the DFS traversal

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            traversal.append(node)

            # Push neighbors in reverse order to maintain correct DFS order
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return traversal


# Graph DFS Traversal (Recursive)
def dfs_graph_recursive(graph, start, visited=None, traversal=None):
    """
    Perform DFS traversal on a graph represented as an adjacency list (recursive approach).

    Args:
    - graph (dict): Graph represented as an adjacency list.
    - start (int): Starting node for DFS.
    - visited (set): Set to keep track of visited nodes.
    - traversal (list): List to store the DFS traversal.

    Returns:
    - List: DFS traversal of the graph.
    """
    if visited is None:
        visited = set()

    if traversal is None:
        traversal = []

    visited.add(start)
    traversal.append(start)

    # Recur for all unvisited neighbors
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_graph_recursive(graph, neighbor, visited, traversal)

    return traversal
