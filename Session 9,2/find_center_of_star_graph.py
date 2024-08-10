from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        for vertex in edges[0]:
            if vertex in edges[1]:
                return vertex
