from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.color_to_check = image[sr][sc]

        def helper(sr, sc, color):
            if sr < 0 or sr > len(image) - 1 or sc < 0 or sc > len(image[0]) - 1:
                return
            if image[sr][sc] != self.color_to_check or image[sr][sc] == color:
                return
            image[sr][sc] = color
            for row_idx, col_idx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                helper(sr + row_idx, sc + col_idx, color)

        helper(sr, sc, color)
        return image
