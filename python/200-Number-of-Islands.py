class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid) 
        cols = len(grid[0])
        island = 0


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    self.dfs(i, j, grid)
                    island += 1
        return island


    def dfs(self, r, c, grid):
        if not grid:
            return
        if (r < 0 or c < 0 or
        r >= len(grid) or c >= len(grid[0]) or
        grid[r][c] != '1'):
            return 

        grid[r][c] = "x"
        self.dfs(r + 1, c, grid)
        self.dfs(r - 1, c, grid)
        self.dfs(r, c + 1, grid)
        self.dfs(r, c - 1, grid)
             

# Time Complexity: O(m×n)
# Space Complexity: O(m×n) due to the recursive depth in the worst case
