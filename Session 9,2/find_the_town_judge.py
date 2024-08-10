from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        checker = [0] * (n + 1)

        for person1, person2 in trust:
            checker[person1] -= 1
            checker[person2] += 1

        for i in range(1, len(checker)):
            if checker[i] == n - 1:
                return i

        return -1
