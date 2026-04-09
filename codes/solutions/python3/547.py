from collections import defaultdict
from typing import List


class Solution:
    def findCircleNum(self, m):
        res, n = 0, len(m)

        def explore(i):
            m[i][i] = 0
            for j in range(n):
                if i != j and m[i][j] == m[j][j] == 1: explore(j)

        for i in range(n):
            if m[i][i] == 1: explore(i); res += 1
        return res


class Solution1:
    def findCircleNum(self, m: List[List[int]]) -> int:
        parent = list(range(len(m)))

        def find(node):
            while node != parent[node]:
                node = parent[node]
            return node

        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            if p1 != p2:
                parent[p1] = p2  # diff set

        for i in range(len(m)):
            for j in range(len(m[0])):
                union(i, j)
        dict_pair = defaultdict(list)

        for idx, val in enumerate(parent):
            dict_pair[find(val)].append(idx)

        print(len(dict_pair.keys()))


isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
Solution1().findCircleNum(isConnected)
