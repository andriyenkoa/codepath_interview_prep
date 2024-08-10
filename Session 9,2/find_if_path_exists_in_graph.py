import collections
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for v, u in edges:
            graph[v].append(u)
            graph[u].append(v)

        def dfs(node, visited):
            if node == destination:
                return True

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor, visited):
                        return True

            return False

        visited = set()
        return dfs(source, visited)
