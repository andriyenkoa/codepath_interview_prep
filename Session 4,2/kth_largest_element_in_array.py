import heapq
from typing import List


class Solution:
    def findKthLargest2(self, nums: List[int], k: int) -> int:

        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)

        return heapq.heappop(nums)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        for _ in range(k):
            num = heapq.heappop(heap)
        return -num
