from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        adj_matrix = [[float('inf') for _ in range(26)] for _ in range(26)]
        for o, c, cost in zip(original, changed, cost):
            adj_matrix[ord(o) - ord('a')][ord(o) - ord('a')]=0
            adj_matrix[ord(c) - ord('a')][ord(c) - ord('a')] = 0
            adj_matrix[ord(o) - ord('a')][ord(c) - ord('a')] = cost

        def floyd_warshall(graph):
            """
            Finds all-pairs shortest paths using the Floyd-Warshall algorithm.
            The graph is represented as an adjacency matrix.
            """
            V = len(graph)
            dist = [row[:] for row in graph]  # Copy the graph matrix

            for k in range(V):
                for i in range(V):
                    for j in range(V):
                        # Update the shortest path if a shorter path is found via intermediate vertex k
                        if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            return dist

        dist = floyd_warshall(adj_matrix)

        cost_min = sum(dist[ord(s) - ord('a')][ord(t) - ord('a')] for s, t in zip(source, target))
        return cost_min if cost_min!=float('inf') else -1


source = "abcd"
target = "acbe"
original = ["a"]
changed = ["e"]
cost = [10000]
res = Solution().minimumCost(source, target, original, changed, cost)
print(res)
