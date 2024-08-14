from collections import defaultdict
from typing import List

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def dfs(x, visited):
            if x not in visited:
                visited.add(x)
                for c in graph[x]:
                    dfs(c, visited)

        graph = defaultdict(list)
        for i, (x1, y1, rad) in enumerate(bombs):
            for j, (x2, y2, _) in enumerate(bombs):
                if i != j and (x1 - x2) ** 2 + (y1 - y2) ** 2 <= rad ** 2:
                    graph[i].append(j)
        res = 0
        print(graph)
        for i in range(len(bombs)):
            visited = set()
            dfs(i, visited)
            res = max(len(visited), res)
        return res

bombs=[[2,1,3],[6,1,4]]
Solution().maximumDetonation(bombs)