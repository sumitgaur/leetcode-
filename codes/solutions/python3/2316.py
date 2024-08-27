from collections import defaultdict
from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()

        def dfs(u):
            if u not in visited:
                visited.add(u)
                for v in adj[u]:
                    dfs(v)

        rem = n
        pairs = 0
        for u in range(n):
            if u not in visited:
                l1 = len(visited)
                dfs(u)
                l2 = len(visited)
                len_ = (l2 - l1)
                pairs += len_ * (rem - len_)
                rem -= len_
        return pairs
