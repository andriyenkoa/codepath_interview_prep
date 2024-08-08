from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        start, end = 0, len(matrix) - 1
        carry = 0
        while start < end:
            while start < (end - carry):
                matrix[start][start + carry], matrix[start + carry][end], \
                    matrix[end][end - carry], matrix[end - carry][start] = \
                    matrix[end - carry][start], matrix[start][start + carry], \
                        matrix[start + carry][end], matrix[end][end - carry]

                carry += 1
            start += 1
            end -= 1
            carry = 0
