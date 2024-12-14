class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posdiag = set()
        negdiag = set()
        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                cpy = ["".join(row) for row in board]
                res.append(cpy)
                return
            
            for c in range(n):
                if c in cols or (r - c) in negdiag or (r + c) in posdiag:
                    continue

                cols.add(c)
                posdiag.add(r + c)
                negdiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                cols.remove(c)
                posdiag.remove(r + c)
                negdiag.remove(r - c)
                board[r][c] = "."
        
        backtrack(0)
        return res

# tutorial link: https://www.youtube.com/watch?v=Ph95IHmRp5M
# time complexity: O(n!)
# space complexity: O(n!)
# check note
        
