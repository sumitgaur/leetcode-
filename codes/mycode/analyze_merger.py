def analyze_merger(N, merges):
    parents = list(range(N))

    def union(u, v):
        p1 = find(u)
        p2 = find(v)
        if p1 != p2:
            parents[p1] = p2

    def find(u):
        while u != parents[u]:
            u = parents[u]
        return u

    for merge in merges:
        union(merge[0], merge[1])

    return sum(1 for u in range(N) if u == parents[u])


N = 5
merges = [(0, 1), (1, 2)]
print(analyze_merger(N, merges))
