from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        N = len(nums)
        result = [None for _ in range(N + 1)]

        result[N], result[N - 1] = 0, nums[N - 1]

        for i in range(N - 2, -1, -1):
            result[i] = max(result[i + 1], result[i + 2] + nums[i])

        return result[0]
