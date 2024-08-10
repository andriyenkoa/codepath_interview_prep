from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1], [1, 1]]
        if numRows < 3:
            return result[:numRows]

        for i in range(2, numRows):
            to_add = [1] * (i + 1)
            array_to_sum = result[i - 1]
            sl, sr = 0, 1
            while sr < len(array_to_sum):
                to_add[sr] = array_to_sum[sl] + array_to_sum[sr]
                sl += 1
                sr += 1
            result.append(to_add)
        return result
