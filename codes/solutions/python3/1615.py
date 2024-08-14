from collections import defaultdict, Counter


def maximalNetworkRank(n: int, roads):
    adj = defaultdict(list)
    counter = Counter()
    for u, v in roads:
        adj[u].append(v)
        adj[v].append(u)
        counter[u] += 1
        counter[v] += 1
    mx_rank = 0
    for i in range(n):
        for j in range(i + 1, n):
            rank = counter[i] + counter[j] - (j in adj[i])
            mx_rank = max(rank, mx_rank)
    return mx_rank


roads = [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]
print(maximalNetworkRank(8, roads))
