import collections


class Solution:
    def treeDiameter(self, edges: List[List[int]], move: int = 0) -> int:
        graph = collections.defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        bfs = {(u, None) for u, nex in graph.items() if len(nex) == 1}
        while bfs:
            bfs, move = (
                {(v, u) for u, pre in bfs for v in graph[u] if v != pre},
                move + 1,
            )
        return max(move - 1, 0)

    def treeDiameter1(self, edges):
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u] = v
            graph[v] = u

        visited = set()
        farthest = None
        far_dist = -1

        def dfs(u, t):
            nonlocal far_dist
            if t > far_dist:
                far_dist = t
                farthest = u
            visited.add(u)
            for v in graph[u]:
                dfs(v, t + 1)
            visited.remove(u)

        dfs(0, 0)
        farthest = None
        far_dist = -1
        dfs(farthest, 0)
        return far_dist

