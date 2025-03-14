class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or c < 0 or
            r >= row or c >= col or
            word[i] != board[r][c] or
            (r,c) in path):
                return False

            path.add((r,c))

            res = (dfs(r, c + 1, i + 1) or
            dfs(r, c - 1, i + 1) or
            dfs(r + 1, c, i + 1) or
            dfs(r - 1, c, i + 1))

            path.remove((r,c))

            return res
        
        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
        
        return False
            
            
# Tutorial link: https://www.youtube.com/watch?v=pfiQ_PS1g8E
# Time Complexity: O(row×col×4^len(word))
# Space Complexity: O(len(word))
