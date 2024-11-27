class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [0] * numCourses

        for dependent, must in prerequisites:
            graph[dependent].append(must)

        def dfs(node):
            state = states[node]
            
            if state == VISITED: return True
            elif state == VISITING: return False

            states[node] = VISITING

            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            states[node] = VISITED
            return True

        for i in range(numCourses):
            if not dfs(i): return False

        return True

    
# tutorial link: https://www.youtube.com/watch?v=nz5V5pOiT8w
# time complexity: O(N+E)
# space complexity: O(N+E)
# check note
