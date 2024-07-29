from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}

        for i in range(len(nums)):
            if nums[i] in checked:
                return [i, checked[nums[i]]]
            checked[target - nums[i]] = i
