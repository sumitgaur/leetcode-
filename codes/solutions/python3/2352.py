from typing import List
from collections import defaultdict


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        mp = defaultdict(int)
        c = 0
        # rows
        for r in grid:
            mp[tuple(r)] += 1
        # columns
        for t in zip(*grid):
            t_tuple = tuple(t)
            if t_tuple in mp:
                c += mp[t_tuple]
        return c


grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]

x = Solution().equalPairs(grid)
print(x)
