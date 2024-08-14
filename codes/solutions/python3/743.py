import collections
import heapq
import sys
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times, N, K):
        q, t, adj = [(0, K)], {}, collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        while q:
            time, node = heapq.heappop(q)
            if node not in t:
                t[node] = time
                for v, w in adj[node]:
                    heapq.heappush(q, (time + w, v))
        return max(t.values()) if len(t) == N else -1

    def networkDelay(self,times,n,k):
        graph=collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        dist = [sys.maxsize] * (n + 1)
        dist[k] = 0
        def dfs(graph,u):
            for v,w in graph[u]:
                if dist[u]+w<dist[v]:
                    dist[v] = dist[u] + w
                    dfs(graph,v)
        dfs(graph,k)
        mx=max(dist[1:])
        return mx if mx<sys.maxsize else -1




times=[[2,1,1],[2,3,1],[3,4,1]]
n,k=4,2
print(Solution().networkDelay(times,n,k))