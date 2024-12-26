from collections import deque

def bfs(graph, start):
    traversal = []
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        traversal.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


    return traversal

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}

#     0
#    / \
#   1   2
#  / \
# 3   4


# print("BFS Traversal:", bfs(graph, 0))


def dfs_recursive(graph, start, visited = None, traversal = None):
    if visited is None:
        visited = set()
    if traversal is None:
        traversal = []

    visited.add(start)
    traversal.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, traversal)
    
    return traversal

# Recursive DFS
# print("DFS Recursive Traversal:", dfs_recursive(graph, 0))


def dfs_iterative(graph, start):
    stack = [start]
    visited = set()
    traversal = []


    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            traversal.append(node)

        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)
        
    return traversal

# print("DFS Iterative Traversal:", dfs_iterative(graph, 0))





### BFS for Tree Representation

def bfs_tree(graph):
    if not graph:
        return []

    traversal = []
    queue = deque([0])  # Start with the root node at index 0

    while queue:
        index = queue.popleft()

        # If the current node is not None, process it
        if graph[index] is not None:
            traversal.append(graph[index])

            # Calculate left and right children
            left = 2 * index + 1
            right = 2 * index + 2

            # Add valid children to the queue
            if left < len(graph):
                queue.append(left)
            if right < len(graph):
                queue.append(right)

    return traversal

graph = [0, 1, 2, 3, 4]
# print("BFS Tree Traversal:", bfs_tree(graph))


### DFS (Recursive) for Tree Representation

def dfs_tree_recursive(graph, index=0, traversal=None):
    if traversal is None:
        traversal = []

    if index >= len(graph):  # If index is out of bounds, return
        return traversal

    traversal.append(graph[index])  # Process the current node

    # Visit left child
    dfs_tree_recursive(graph, 2 * index + 1, traversal)
    # Visit right child
    dfs_tree_recursive(graph, 2 * index + 2, traversal)

    return traversal


# print("DFS Recursive Tree Traversal:", dfs_tree_recursive(graph))


### DFS (Iterative) for Tree Representation

def dfs_tree_iterative(graph):
    if not graph:
        return []

    stack = [0]  # Start with the root node at index 0
    traversal = []

    while stack:
        index = stack.pop()
        traversal.append(graph[index])

        # Push right child first (so left child is processed first)
        right = 2 * index + 2
        left = 2 * index + 1

        if right < len(graph):
            stack.append(right)
        if left < len(graph):
            stack.append(left)

    return traversal


# print("DFS Iterative Tree Traversal:", dfs_tree_iterative(graph))
