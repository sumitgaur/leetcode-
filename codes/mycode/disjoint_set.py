import heapq


class DisjointSet:
    """
    Implemented as forest of trees
    """

    def __init__(self, n):
        self.parents = list(range(n))

    def find(self, x):
        """
        Return the topmost element in the disjoint set tree
        O(lgn)
        :param x:
        :return:
        """
        if x != self.parents[x]:
            self.find(self.parents[x])
        return x

    def union(self, p1, p2):
        """
        Union two disjoint sets
        :param p1:
        :param p2:
        :return:
        """
        self.parents[p1] = p2

    def components(self):
        visited = [False] * len(self.parents)

        def visit(x):
            visited[x] = True
            if self.parents[x] != x:
                return [x] + visit(self.parents[x])
            return [x]

        components = []
        for i in range(len(self.parents)):
            if not visited[i]:
                components.append(visit(i))

        return components


# A class to represent a disjoint set
class DisjointSet2:
    parent = {}

    # perform MakeSet operation
    def makeSet(self, universe):
        # create `n` disjoint sets (one for each item)
        for i in range(universe):
            self.parent[i] = i

    # Find the root of the set in which element `k` belongs
    def Find(self, k):
        # if `k` is root
        if self.parent[k] == k:
            return k
        # recur for the parent until we find the root
        return self.Find(self.parent[k])
    # Perform Union of two subsets
    def Union(self, a, b):
        # find the root of the sets in which elements
        # `x` and `y` belongs
        x = self.Find(a)
        y = self.Find(b)

        self.parent[x] = y


dsu=DisjointSet2()
dsu.makeSet(100)
edges=[[1,2],[1,3],[2,3]]
for u,v in edges:
    x=dsu.Find(u)
    y=dsu.Find(v)
    if x==y:
        return [u,v]
        dsu.Union(u,v)
    return None
