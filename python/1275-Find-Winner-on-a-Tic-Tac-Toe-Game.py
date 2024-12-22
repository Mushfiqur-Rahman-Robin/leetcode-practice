class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[""] * 3 for _ in range(3)]

        for idx, (r, c) in enumerate(moves):
            board[r][c] = 'A' if idx % 2 == 0 else 'B'

        for i in range(len(board)):
            for j in range(len(board)):
                if i + 2 < len(board) and board[i][j] == board[i+1][j] == board[i+2][j] != "":
                    return board[i][j]

                if j + 2 < len(board) and board[i][j] == board[i][j+1] == board[i][j+2] != "":
                    return board[i][j]

                if i + 2 < len(board) and j + 2 < len(board) and board[i][j] == board[i+1][j+1] == board[i+2][j+2] != "":
                    return board[i][j]

                if i + 2 < len(board) and j - 2 >= 0 and board[i][j] == board[i+1][j-1] == board[i+2][j-2] != "":
                    return board[i][j]

        if len(moves) == 9:
            return "Draw"

        return "Pending"


# time complexity: O(1)
# space complexity: O(1)
# check note
