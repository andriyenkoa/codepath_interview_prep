from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        checked = {}

        for path in paths:
            checked[path[0]] = path[1]

        dest = paths[0][1]
        while dest in checked.keys():
            dest = checked[dest]

        return dest
