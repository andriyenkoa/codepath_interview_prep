from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        touchesAtlantic = set()
        touchesPacific = set()

        def dfs(r, c, touchesOcean, prevHeight):
            if r < 0 or r >= len(heights) or c < 0 or c >= len(heights[0]) or (r, c) in touchesOcean:
                return

            if heights[r][c] >= prevHeight:
                touchesOcean.add((r, c))

                for row_idx, col_idx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    dfs(r + row_idx, c + col_idx, touchesOcean, heights[r][c])

        for i in range(len(heights[0])):
            dfs(0, i, touchesPacific, 0)
            dfs(len(heights) - 1, i, touchesAtlantic, 0)

        for i in range(len(heights)):
            dfs(i, 0, touchesPacific, 0)
            dfs(i, len(heights[0]) - 1, touchesAtlantic, 0)

        return list(touchesPacific & touchesAtlantic)
