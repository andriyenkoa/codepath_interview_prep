from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_queue = deque()
        fresh_cnt = 0
        count = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        rows = len(grid)
        if not rows:
            return -1
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten_queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_cnt += 1
        result = 0

        while rotten_queue and fresh_cnt > 0:
            result += 1
            for _ in range(len(rotten_queue)):
                rottren_row_idx, rotten_col_idx = rotten_queue.popleft()
                for row, col in count:
                    row_idx, col_idx = rottren_row_idx + row, rotten_col_idx + col
                    if row_idx < 0 or row_idx == rows or col_idx < 0 or col_idx == cols:
                        continue
                    if grid[row_idx][col_idx] == 2 or grid[row_idx][col_idx] == 0:
                        continue
                    fresh_cnt -= 1

                    grid[row_idx][col_idx] = 2

                    rotten_queue.append((row_idx, col_idx))

        return result if fresh_cnt == 0 else -1