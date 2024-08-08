from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.count = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def helper(grid, row_idx, col_idx):
            if row_idx < 0 or row_idx > len(grid) - 1 or col_idx < 0 or col_idx > len(grid[0]) - 1:
                return
            if grid[row_idx][col_idx] == "0" or \
                    grid[row_idx][col_idx] == "2":
                return

            grid[row_idx][col_idx] = "2"
            for row, col in self.count:
                helper(grid, row_idx + row, col_idx + col)

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    helper(grid, i, j)
                    result += 1

        return result
