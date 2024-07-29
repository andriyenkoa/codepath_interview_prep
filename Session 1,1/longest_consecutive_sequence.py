from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        max_val = 0

        for num in unique_nums:
            if num - 1 not in unique_nums:
                cur_max = 1
                while num + 1 in unique_nums:
                    num += 1
                    cur_max += 1
                max_val = max(max_val, cur_max)

        return max_val


