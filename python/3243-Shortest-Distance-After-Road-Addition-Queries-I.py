class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = [[i+1] for i in range(n)]
        
        def shortest_path(): # bfs
            q = deque()
            q.append((0, 0)) # node, length to reach that node
            visited = set()
            visited.add((0,0)) # for some edge cases

            while q:
                curr, length = q.popleft()
                if curr == n - 1:
                    return length
                for nei in adj[curr]:
                    if nei not in visited:
                        q.append((nei, length + 1))
                        visited.add(nei)
                
        res = []
        for src, dst in queries:
            adj[src].append(dst)
            res.append(shortest_path())
        
        return res

# tutorial link: https://www.youtube.com/watch?v=zCeZOyACpUQ
# time complexity:  O(m * (n + m))
# space complexity: O(n + m)
# check note
