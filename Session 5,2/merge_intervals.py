from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        for low, high in sorted(intervals):
            if not result:
                result.append([low, high])
            else:
                cur_high = result[-1][1]
                if cur_high >= low:
                    result[-1][1] = max(high, cur_high)
                else:
                    result.append([low, high])
        return result
