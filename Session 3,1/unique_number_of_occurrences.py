from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = {}

        for one_num in arr:
            if one_num in counter:
                counter[one_num] += 1

            else:
                counter[one_num] = 1

        return len(set(counter.values())) == len(counter.values())
