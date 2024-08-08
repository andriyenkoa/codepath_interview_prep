from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        start_row, end_row = 0, len(matrix) - 1
        start_col, end_col = 0, len(matrix[0]) - 1
        result = []
        while start_col <= end_col and start_row <= end_row:
            for i in range(start_col, end_col + 1):
                result.append(matrix[start_row][i])
            start_row += 1
            for i in range(start_row, end_row + 1):
                result.append(matrix[i][end_col])
            end_col -= 1
            if start_row <= end_row:
                for i in range(end_col, start_col-1, -1):
                    result.append(matrix[end_row][i])
                end_row -= 1
            if start_col <= end_col:
                for i in range(end_row, start_row-1, -1):
                    result.append(matrix[i][start_col])
                start_col += 1
        return result
