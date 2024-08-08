from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix[0])
        columns = len(matrix)

        result = [[] for _ in range(rows)]

        for i in range(columns):
            for j in range(rows):
                result[j].append(matrix[i][j])

        return result
