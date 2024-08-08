from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.count = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def helper(grid, row_idx, col_idx):
            if row_idx < 0 or row_idx > len(grid) -1 or col_idx < 0 or col_idx > len(grid[0]) - 1:
                return 0
            if grid[row_idx][col_idx] != 1:
                return 0
            grid[row_idx][col_idx] = 2
            res = 0
            for row, col in self.count:
                res += helper(grid, row_idx + row, col_idx + col)
            return 1 + res

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, helper(grid, i, j))

        return max_area
