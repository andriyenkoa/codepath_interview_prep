import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            temp_h = 0
            for pile in piles:
                temp_h += math.ceil(pile / mid)
            if temp_h <= h:
                right = mid
            elif temp_h > h:
                left = mid + 1
        return left
