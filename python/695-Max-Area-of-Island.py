class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                grid[r][c] == 0):
                return 0
            
            grid[r][c] = 0  # grid[r][c] = 0 prevents revisiting cells, effectively marking them as visited.
            res = 1 + dfs(r + 1, c) + dfs(r - 1, c) + \
                    dfs(r, c + 1) + dfs(r, c - 1)
            # Count the current cell as 1 and add the area of neighboring cells
            
            return res
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        
        return max_area

# time complexity: O(rows * cols)
# space complexity: O(rows * cols)
# check note
        
