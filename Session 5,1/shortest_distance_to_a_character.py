from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        def helper(i,distance):
            if i < 0 or i > len(s) - 1 or output[i] <= distance:
                return

            output[i] = distance
            helper(i+1, distance+1)
            helper(i-1, distance+1)
        output = [len(s) for _ in s]
        for i,char in enumerate(s):
            if char == c:
                helper(i,0)
        return output
