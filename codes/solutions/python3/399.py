from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]]
    ) -> List[float]:

        graph = defaultdict(list)

        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        def dfs(x, y, visited):
            if x not in graph:
                return -1.0

            if x == y:
                return 1.0

            visited.add(x)

            for nei, val in graph[x]:
                if nei not in visited:
                    result = dfs(nei, y, visited)
                    if result != -1:
                        return val * result

            return -1.0

        res = []

        for a, b in queries:
            res.append(dfs(a, b, set()))

        return res
