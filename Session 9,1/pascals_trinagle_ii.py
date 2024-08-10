from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1, 1]
        if rowIndex < 2:
            return res[:rowIndex+1]

        curIndex = 1
        while curIndex < rowIndex:
            curIndex += 1
            cur_res = [1] * (curIndex + 1)
            left, right = 0, 1
            while right < len(res):
                cur_res[right] = res[left] + res[right]
                left += 1
                right += 1
            res = cur_res
        return res
