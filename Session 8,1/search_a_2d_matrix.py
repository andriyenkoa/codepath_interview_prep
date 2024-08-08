from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, len(matrix) - 1
        while start <= end:
            mid = (start + end) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            elif target < matrix[mid][0]:
                end = mid - 1
            else:
                start = mid + 1
        result_row = mid
        start, end = 0, len(matrix[0]) - 1
        while start <= end:
            mid = (start + end) // 2
            if matrix[result_row][mid] == target:
                return True
            elif matrix[result_row][mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return matrix[result_row][mid] == target
