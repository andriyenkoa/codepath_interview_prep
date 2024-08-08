from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        self.count = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def helper(board, row_idx, col_idx):
            if row_idx < 0 or row_idx > len(board) - 1 or col_idx < 0 or col_idx > len(board[0]) - 1:
                return
            if board[row_idx][col_idx] != 'X':
                return

            board[row_idx][col_idx] = "."
            for row, col in self.count:
                helper(board, row_idx + row, col_idx + col)

        res = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    res += 1
                    helper(board, i, j)
        return res
