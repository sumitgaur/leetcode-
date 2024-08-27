class Solution:
    def countComponents(self, n, edges):
        visited, res, adj = set(), 0, collections.defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        def dfs(i):
            visited.add(i)
            for v in adj[i]:
                if v not in visited:
                    dfs(v)

        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        return res

    def countComponents1(self, n, edges):
        parents = list(range(n))

        def union(u, v):
            p1 = find(u)
            p2 = find(v)
            if p1 != p2:
                parents[p1] = p2

        def find(u):
            while u != parents[u]:
                u = parents[u]
            return u

        for u, v in edges:
            union(u, v)

        return sum(1 for u in range(n) if parents[u] == u)


n = 5
edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

print(Solution().countComponents1(n, edges))
